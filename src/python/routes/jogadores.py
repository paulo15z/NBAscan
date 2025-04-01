# endpoint para stats de jogadores

from fastapi import APIRouter, HTTPException
import sqlite3
from src.python.app import DB_PATH, processar_dados

router = APIRouter(prefix="/jogadores", tags=["jogadores"])

@router.get("/{id}/estatisticas")
def get_estatisticas(id: int):
    #conecta com o banco primeiro
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    #procurando o jogador pelo ID dele
    cursor.execute("SELECT nome, equipe FROM jogadores WHERE id = ?", (id,))
    jogador = cursor.fetchone()
    if not jogador:
        conexao.close()
        raise HTTPException(status_code=404, detail="Jogador não encontrado :(")
    
    nome, equipe = jogador
    
    # procurar os pontos do jogador na tabela estatisticas
    cursor.execute("SELECT pontos FROM estatisticas WHERE jogador_id = ?", (id,))
    pontos_rows = cursor.fetchall()
    conexao.close()

    if not pontos_rows:
        raise HTTPException(status_code=404, detail="Nenhuma estatistica encontrada para esse jogador :(")
    
    #puxa os pontos como uma list
    pontos = [row[0] for row in pontos_rows]
    #usa o processamento em C
    resultado = processar_dados(pontos)

    return {
        "jogador_id": id,
        "nome": nome,
        "equipe": equipe,
        "pontos": pontos,
        "media": resultado["media"],
        "maximo": resultado["maximo"]
    }