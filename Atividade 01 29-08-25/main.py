# Exercícios de Lista

# No início do seu arquivo Python
# -*- coding: utf-8 -*-


#01. Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# print(livros)


#----------------------------------------------------------------------------------------------------------------
#02. Usando a lista livros, exiba apenas o primeiro e o último elemento

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# print(livros[0]+'\n' + livros[2])
# print(livros[0], livros[-1], sep='\n')



#----------------------------------------------------------------------------------------------------------------
#03. Adicione mais dois livros á lista livros usando o método append() e exiba a lista atualizada

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# livros.append('O senhor dos anéis')
# livros.append('O médico e o monstro')

# print(livros)



#----------------------------------------------------------------------------------------------------------------
#04.Insira o livro "Duna" na segunda posição da lista usando insert()

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# livros.insert(1, 'Duna')

# print(livros)


#----------------------------------------------------------------------------------------------------------------
#05. Remova o livros "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado"

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# if 'Silêncio dos inocentes' in livros:
#     livros.remove('Silêncio dos inocentes')
# else:
#     print('Livro não encontrado')
# OR
# try:
#     livros.remove('Silêncio dos inocentes')
# except ValueError:
#     print('Livro não encontrado')
#     print(livros)


#----------------------------------------------------------------------------------------------------------------
#06. Crie uma lista chamada números com os valores [1,2,3,2,4,2,5]. Mostre quantas vezes o número 2 aparece na lista

# numeros = [1,2,3,2,4,2,5]

# print(numeros.count(2))


#----------------------------------------------------------------------------------------------------------------
#07. Percorra a lista livros e exiba cada livro com a frase. "O livro <nome do livro> é interessante"

# livros = ['Hamlet','Frankenstein','Alice no País das Maravilhas' ]
# for livro in livros:
#     print(f'O livro {livro} é interessante.')



#----------------------------------------------------------------------------------------------------------------
#08. Dada a lista idades = [12,18,25,13,30]. Use um laço para exibir somente as idades maiores ou iguais a 18

# idades = [12,18,25,13,30]

# for i in idades:
#     if i >= 18:
#         print(i)
    
      


#----------------------------------------------------------------------------------------------------------------
#09. Crie uma lista valores = [10,20,30,40]. Use um laço for para calcular manualmente a soma de todos os valores

# valores = [10,20,30,40]
# soma = 0
# for i in valores:
#     soma += i
# print('O valor da soma é:',soma)

#----------------------------------------------------------------------------------------------------------------
#10. Use input para receber 3 notas de dois alunos. Às notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo: notas[[7,8,9],[6,5,7]]. No fim imprima a média de cada aluno

# notas =[]

# nota1= float(input("Digite a primeira nota do Aluno1: "))
# nota2= float(input("Digite a segunda nota do Aluno1: "))
# nota3= float(input("Digite a terceira nota do Aluno1: "))

# aluno1 = [nota1,nota2,nota3]
# print('')
# notas.append(aluno1)

# nota1= float(input("Digite a primeira nota do Aluno2: "))
# nota2= float(input("Digite a segunda nota do Aluno2: "))
# nota3= float(input("Digite a terceira nota do Aluno2: "))

# aluno2 = [nota1,nota2,nota3]

# notas.append(aluno2)
# print('')
# for i, aluno in enumerate(notas, start=1):
#     media = sum(aluno) / len(aluno)
#     print (f'A média do Aluno {i} é: {media:.2f}')

# OR


# notas = []
# for i in range(2):
#     print(f"Digite as notas do aluno {i+1}:")
#     aluno = [float(input(f"Digite a nota {j+1}: ")) for j in range(3)]
#     notas.append(aluno)

# for i, aluno in enumerate(notas, start=1):
#     media = sum(aluno) / len(aluno)
#     print(f"A média do aluno {i} é: {media:.2f}")




#----------------------------------------------------------------------------------------------------------------
#11. Usando list comprehension, crie um tabuleiro de xadrez vázio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma: [] - para posições vazias, tor - para a torre, cav - para o cavalo, bis - para o bispo, rai - para a rainha, rei - para o rei, pea - para o peão. Por fim imprima na tela, deixando cada linha da matriz abaixo da outra. (Dica: você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

# import numpy as np
# print(np.__version__)
# pip install numpy

# tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

# tabuleiro[0] = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
# tabuleiro[1] = ['pea'] * 8
# tabuleiro[6] = ['pea'] * 8
# tabuleiro[7] = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
## tabuleiro[7][3], tabuleiro[7][4] = tabuleiro[7][4], tabuleiro[7][3]
# tabuleiro_np = np.array(tabuleiro)

# for linha in tabuleiro_np:
#     print(' '.join(linha))
