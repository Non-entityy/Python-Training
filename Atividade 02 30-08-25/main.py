# Exercícios de dicionários

# 1. Crie um dicionário simples
# Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.

# aluno = {
#     "nome": "Lucas",
#     "idade": 18,
#     "nota": 7.8
# }
# print(aluno)



#--------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Acessando valores
# Dado o dicionário:
# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.

# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

# print(f'Nome: {produto["nome"]}, Quantidade: {produto["estoque"]}')

#--------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Adicionando novos pares chave-valor
# Dado o dicionário:
# pessoa = {"nome": "Carlos", "idade": 30}
# Adicione uma nova chave "cidade" com valor "São Paulo".

# pessoa = {"nome": "Carlos", "idade": 30}
# pessoa["Cidade"] = "São Paulo"
# print(pessoa)

#--------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Removendo elementos
# Dado o dicionário:
# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.

# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# # del carro["ano"] 
# #OR
# ano_removido = carro.pop("ano")
# print(carro)
# print(ano_removido)



#--------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Verificando existência de uma chave
# Verifique se a chave "telefone" existe no dicionário:
# contato = {"nome": "Ana", "email": "ana@email.com"}

# contato = {"nome": "Ana", "email": "ana@email.com"}
# if "telefone" in contato:
#      print('A chave "telefone" existe.')
# else:
#      print('A chave "telefone" não existe.')

# #OR

# if contato.get("telefone") is not None:
#     print('A chave "telefone" existe.')
# else:
#     print('A chave "telefone" não existe.')


#--------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Contando frequência de palavras
# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# def contar_frequncia(palavras):
#     contagem = {}
#     for palavra in palavras:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#     return contagem
# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
# frequencia = contar_frequncia(palavras)
# print(frequencia)

#--------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Invertendo um dicionário
# Dado o dicionário:
# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.

# d = {"a": 1, "b": 2, "c": 3}
# d_inverso = {valor: chave for chave, valor in d.items()}
# print(d_inverso)


#--------------------------------------------------------------------------------------------------------------------------------------------------
# 8. Dicionário com listas
# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

# alunos = {
#     "Lucas": [7.6, 6.7, 8.0],
#     "Ana": [9.5, 6.4, 9.7],
#     "Pedro": [6.5, 5.6, 8.5]
# }

# for nome, notas in alunos.items():
#     media = sum(notas) / len(notas)
#     print(f'{nome} - Média: {media:.2f}')

#--------------------------------------------------------------------------------------------------------------------------------------------------
# 9. Mesclando dois dicionários
# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

# def mesclar_dic(dic1,dic2):
#     resultado = dic1.copy()
#     resultado.update(dic2)
#     return resultado

# d1 ={"a": 1, "b": 2}
# d2 ={"b": 4, "c": 5}

# d_mesc = mesclar_dic(d1,d2)
# print(d_mesc)

#--------------------------------------------------------------------------------------------------------------------------------------------------
# 10. Ordenando dicionário por valor
# Dado o dicionário:
# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# ordenado = sorted(pontuacoes.items(), key= lambda item: item[1], reverse= True)

# for nome, pontos in ordenado:
#     print(f'{nome}: {pontos}')
