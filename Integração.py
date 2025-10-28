import sqlite3 
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
print("Lista de alunos:")
for aluno in alunos:
    print(aluno)

# conexao = sqlite3.connect("escola_v2.db")
# cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM Aluno;")
total = cursor.fetchone()[0]

print(f"Total de alunos cadastrados: {total}")


conexao.close()
