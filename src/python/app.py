# arquivo principal
from nba_api.stats.static import teams
import sqlite3
import json
import ctypes

DB_PATH = "data/nba_scan.db" 

# carregar a biblioteca em C
try:
    lib = ctypes.CDLL("./src/c/processamento.dll")
except OSError as e:
    print(f"Erro ao carregar a DLL: {e}")
    exit(1)

#configurar os tipos de retorno e argumentos das funçoes no processamento.c
lib.calcular_media.restype = ctypes.c_float # determinando como FLOAT
lib.calcular_media.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

lib.encontrar_maximo.restype = ctypes.c_int
lib.encontrar_maximo.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]


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
    return times

def processar_dados(pontos):
    # CHAMA O PROCESSAMENTO.C 
    tamanho = len(pontos)
    array_pontos = (ctypes.c_int * tamanho)(*pontos) #converte a lista em array

    media = lib.calcular_media(array_pontos, tamanho)
    maximo = lib.encontrar_maximo(array_pontos, tamanho)

    return {"media": media, "maximo": maximo}

