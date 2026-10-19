import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("coinbase5.db")
    cursor = conexao.cursor()

    cursor.execute("""
          CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT,
            preco REAL,
            data_hora TEXT
        )            
    """)
    conexao.commit()
    conexao.close()

def inserir_preco(moeda,preco,data_hora):
    conexao = sqlite3.connect("coinbase5.db")
    cursor = conexao.cursor()

    cursor.execute("""
            INSERT INTO precos(moeda,preco,data_hora)
            VALUES(?,?,?)
    """,(moeda,preco,data_hora))
    conexao.commit()
    conexao.close()