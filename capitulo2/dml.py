import sqlite3
from datetime import date

# Conexão e criação da tabela base (DDL implícita)
con = sqlite3.connect('henriquers-dev.db')
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL,
    data_admissao TEXT
)
''')
con.commit()

# Inserção de registros simulando coleta automatizada
dados = [
    ('Ana Silva', 'Analista de Dados', 5500.0, date.today().isoformat()),
    ('Bruno Lima', 'Engenheiro de Software', 7200.0, date.today().isoformat()),
    ('Carla Souza', 'Cientista de Dados', 8900.0, date.today().isoformat())
]

cur.executemany('''
INSERT INTO funcionarios (nome, cargo, salario, data_admissao)
VALUES (?, ?, ?, ?)
''', dados)

con.commit()
con.close()
