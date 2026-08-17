# Executa o pip para conexão do SQLite
import sqlite3

# Cria e conecta em um banco de dados
conexao = sqlite3.connect('henriquersdev.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Executa uma consulta simples
cursor.execute('SELECT sqlite_version();')

# Exibe o resultado
print("Versão do SQLite:", cursor.fetchone())

# Fecha a conexão
conexao.close()
