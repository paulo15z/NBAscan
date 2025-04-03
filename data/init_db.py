import sqlite3
from nba_api.stats.endpoints import ScoreboardV2
from datetime import datetime

DB_PATH = "data/nba_scan.db"

def buscar_jogos_do_dia():
    # Obtém a data atual no formato YYYYMMDD exigido pela API
    data_atual = datetime.today().strftime('%Y%m%d')

    # Chama a API para obter os jogos do dia
    scoreboard = ScoreboardV2(game_date=data_atual)
    jogos_data = scoreboard.get_dict()["resultSets"]

    # Filtramos os dados certos dentro do JSON retornado
    for result in jogos_data:
        if result["name"] == "GameHeader":  # Pegamos apenas os jogos
            jogos = result["rowSet"]  # Aqui temos os dados dos jogos
            colunas = result["headers"]  # Nomes das colunas para mapeamento
            break
    else:
        print("⚠️ Nenhum jogo encontrado!")
        return []

    # Criamos uma lista de dicionários com os jogos
    jogos_formatados = []
    for jogo in jogos:
        dados = dict(zip(colunas, jogo))  # Mapeia colunas aos valores
        jogos_formatados.append({
            "game_id": dados["GAME_ID"],
            "home_team": dados["HOME_TEAM_ID"],
            "visitor_team": dados["VISITOR_TEAM_ID"],
            "horario": dados["GAME_TIME"],  # Ajustar se necessário
            "status": dados["GAME_STATUS_TEXT"]
        })

    return jogos_formatados

def salvar_jogos_no_banco(jogos):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criamos a tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id TEXT UNIQUE,
            home_team TEXT,
            visitor_team TEXT,
            horario TEXT,
            status TEXT
        )
    """)

    # Inserimos os jogos no banco
    for jogo in jogos:
        try:
            cursor.execute("""
                INSERT INTO jogos (game_id, home_team, visitor_team, horario, status)
                VALUES (?, ?, ?, ?, ?)
            """, (jogo["game_id"], jogo["home_team"], jogo["visitor_team"], jogo["horario"], jogo["status"]))
        except sqlite3.IntegrityError:
            print(f"⚠️ Jogo {jogo['game_id']} já existe no banco.")

    conn.commit()
    conn.close()

# Execução
jogos = buscar_jogos_do_dia()
if jogos:
    salvar_jogos_no_banco(jogos)
    print("✅ Jogos salvos no banco!")
