# Atividade: SQLite no python


# 1. Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db

import sqlite3
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Faça a query para pegar toda a tabela alunos e imprima na tela.
'''
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
print("Lista de alunos: ")
for aluno in alunos:
    print(aluno)
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.
'''
cursor.execute("SELECT nome, (nota1+nota2)/2.0 AS Media_Notas FROM Aluno ORDER BY Media_Notas DESC LIMIT 10")
top10 = cursor.fetchall()
print('Lista dos Tops 10: ')
for i, (nome, media) in enumerate(top10, start= 1):
    print(f"{i}º - {nome} |Média: {media:.2f}")
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
'''

cursor.execute("SELECT * FROM Aluno a LEFT JOIN Turma t on a.id_turma = t.id;")
tabela = cursor.fetchall()
print(f'{"ID":^5}| {"Nome":^20}  | {"Data de Nascimento":^10}| {"Nota 1":^5}| {"Nota 2":^5}| {"Id Turma Aluno":^5}| {"Id Turma":^5} | {"Nome da Turma":^18}| {"Semestre":^5}|{"Ano":^5}| {"Id do Curso":^5}')
for id, nome, data_nascimento, nota1, nota2, id_turma, idt, nome_turma, semestre, ano, id_curso in tabela:
    print(f'{"-"*5}|{"-"*23}|{"-"*19}|{"-"*7}|{"-"*7}|{"-"*15}|{"-"*10}|{"-"*19}|{"-"*9}|{"-"*5}|{"-"*10}\n'
          f'{id:^5}| {nome:^20}  | {data_nascimento:^13}     | {nota1:^4}  | {nota2:^4}  | {id_turma:^5}         | {idt:^5}    | {nome_turma:^18}| {semestre:^6}  | {ano:^2}| {id_curso:^5}')

'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
'''
cursor.execute("SELECT * FROM Aluno a LEFT JOIN Turma t on a.id_turma = t.id WHERE a.id_turma = 2 ")
tabela = cursor.fetchall()
print(f'{"ID":^5}| {"Nome":^20}  | {"Data de Nascimento":^10}| {"Nota 1":^5}| {"Nota 2":^5}| {"Id Turma Aluno":^5}| {"Id Turma":^5} | {"Nome da Turma":^18}| {"Semestre":^5}|{"Ano":^5}| {"Id do Curso":^5}')
for id, nome, data_nascimento, nota1, nota2, id_turma, idt, nome_turma, semestre, ano, id_curso in tabela:
    print(f'{"-"*5}|{"-"*23}|{"-"*19}|{"-"*7}|{"-"*7}|{"-"*15}|{"-"*10}|{"-"*19}|{"-"*9}|{"-"*5}|{"-"*10}\n'
          f'{id:^5}| {nome:^20}  | {data_nascimento:^13}     | {nota1:^4}  | {nota2:^4}  | {id_turma:^5}         | {idt:^5}    | {nome_turma:^10} | {semestre:^6}  | {ano:^2}| {id_curso:^5}')

'''