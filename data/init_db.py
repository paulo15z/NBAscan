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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        equipe TEXT
    )""")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
    print("Banco de dados criado!")
