import sqlite3

def criar_banco():
    conn = sqlite3.connect("data/nba_scan.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_id TEXT UNIQUE,
        data TEXT
    )""")

    # Nova tabela estatisticas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estatisticas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jogador_id INTEGER,
        pontos INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogadores(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        equipe TEXT
    )""")

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS raw_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        json_data TEXT,
        timestamp TEXT
    )""")    

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
    print("Banco de dados criado!")
