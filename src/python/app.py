# arquivo principal

from nba_api.stats.static import teams
import sqlite3
import json
import subprocess

DB_PATH = "nba_scan.db"

def salvar_dados_brutos(dados):
    #SALVA OS DADOS >BRUTOS< NO BANCO DE DADOS
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO raw_data (json_data, timestamp)
        VALUES (?, datetime('now'))
 """, (json.dumps(dados),))
    
    conexao.commit()
    conexao.close()

def listar_times():
    #BUSCA OS TIMES E SALVA RAW NO BANCO DE DADOS
    times = teams.get_teams()
    salvar_dados_brutos(times)

def processar_dados():
    # CHAMA O PROCESSAMENTO.C 
    resultado = subprocess.run(["src/c/processamento"], capture_output=True, text=True)
    print("Resultado do processamento:\n", resultado.stdout)

if __name__ == "__main__":
    listar_times()
    processar_dados()