import sqlite3
import time

# Conecta ou cria o banco de dados da empresa
con = sqlite3.connect('henriquersdev.db')
cur = con.cursor()

print("=== Etapa 1: Criação de Tabelas Principais ===")
cur.execute('''
    CREATE TABLE IF NOT EXISTS departamentos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
        )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        funcao TEXT NOT NULL,
        salario REAL,
        
        departamento_id INTEGER,
        FOREIGN KEY(departamento_id) REFERENCES departamentos(id)
        )
''')

con.commit()
print("Tabelas 'departamentos' e 'funcionarios' criadas com sucesso!\n")
time.sleep(0.3)

# Inserção inicial de dados-base
cur.execute('INSERT OR IGNORE INTO departamentos(nome) VALUES ("Aplicativos para Web")')
cur.execute('INSERT OR IGNORE INTO departamentos(nome) VALUES ("Desenvolvimento de Games")')
cur.execute('INSERT OR IGNORE INTO departamentos(nome) VALUES ("Banco de Dados")')
con.commit()

print("Departamentos inseridos com sucesso!\n")
time.sleep(0.3)

print("=== Etapa 2: Verificação e alteração da estrutura ===")
# Verifica se a coluna 'data_admissao' existe, adiciona caso necessário
colunas = [c[1] for c in cur.execute("PRAGMA table_info(funcionarios)").fetchall()]
if 'data_admissao' not in colunas:
    cur.execute("ALTER TABLE funcionarios ADD COLUMN data_admissao TEXT DEFAULT '2026-10-05'")
    print("Coluna 'data_admissao' adicionada à tabela 'funcionarios'.\n")
else:
    print("A coluna 'data_admissao' já existe. Nenhuma alteração necessária.\n")

# Cria uma nova tabela temporária para controle de projetos
cur.execute('''
CREATE TABLE IF NOT EXISTS projetos_temp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    responsavel TEXT,
    departamento_id INTEGER,
    FOREIGN KEY(departamento_id) REFERENCES departamentos(id)
)
''')
con.commit()
print("Tabela 'projetos_temp' criada para uso temporário.\n")
time.sleep(1)

print("=== Etapa 3: Simulação de reconfiguração e remoção ===")
# Remove a tabela temporária após o uso
cur.execute("DROP TABLE IF EXISTS projetos_temp")
con.commit()
print("Tabela temporária 'projetos_temp' removida com sucesso.\n")

# Reconfigura a tabela principal removendo e recriando com nova estrutura
cur.execute("DROP TABLE IF EXISTS funcionarios")

cur.execute('''
CREATE TABLE funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL,
    data_admissao TEXT,
    avaliacao REAL DEFAULT 0.0
)
''')
con.commit()
print("Tabela 'funcionarios' recriada com nova estrutura incluindo 'avaliacao'.\n")

con.close()
print("Processo de DDL concluído com sucesso!")
