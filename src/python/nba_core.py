# src/python/logic/nba_core.py
from nba_api.stats.static import teams
import sqlite3, json, ctypes

DB_PATH = "data/nba_scan.db"

lib = ctypes.CDLL("./src/c/processamento.dll")
lib.calcular_media.restype = ctypes.c_float
lib.calcular_media.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.encontrar_maximo.restype = ctypes.c_int
lib.encontrar_maximo.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

NBA_TITULOS = {
    "Boston Celtics": 18,
    "Los Angeles Lakers": 17,
    "Golden State Warrios": 7,
    "Chicago Bulls": 6,
    "San Antonio Spurs": 5,
    "Philadelphia 76ers": 3,
    "Detroit Pistons": 3,
    "Miami Heat": 3,
    "New York Knicks": 2,
    "Houston Rockets": 2,
    "Milwaukee Bucks": 2,
    "Cleveland Cavaliers": 1,
    "Atlanta Hawks": 1,
    "Washington Wizards": 1,
    "Oklahoma City Thunder": 1,
    "Portland Trail Blazers": 1,
    "Dallas Mavericks": 1,
    "Sacramento Kings": 1,
    "Toronto Raptors": 1,
    "Denver Nuggets": 1
}

def listar_times_com_titulos():
    all_teams = teams.get_teams()
    lista = []

    for team in all_teams:
        nome = team["full_name"]
        titulos = NBA_TITULOS.get(nome, 0)
        lista.append({
            "nome": nome,
            "titulos": titulos
        })

    lista.sort(key=lambda x: x["titulos"], reverse=True)
    return lista

def salvar_dados_brutos(dados):
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO raw_data (json_data, timestamp) VALUES (?, datetime('now'))", (json.dumps(dados),))
    conexao.commit()
    conexao.close()

def listar_times():
    times = teams.get_teams()
    salvar_dados_brutos(times)
    return times

def processar_dados(pontos):
    tamanho = len(pontos)
    array_pontos = (ctypes.c_int * tamanho)(*pontos)
    media = lib.calcular_media(array_pontos, tamanho)
    maximo = lib.encontrar_maximo(array_pontos, tamanho)
    return {"media": media, "maximo": maximo}

