# Lista de Exercícios: Função lambda (map, filter, reduce, sorted)

# 1. Dobro dos números (map + lambda)
# Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

# lista = [1,2,3,4,5]
# nova_lista = list(map(lambda x: x*2, lista))
# print(nova_lista)

#-------------------------------------------------------------------------------------------------------------------------
# 2. Filtrar pares (filter + lambda)
#  Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.

# lista = [10, 15, 20, 25, 30]
# filtro = list(filter(lambda x: x%2 == 0, lista))
# print(filtro)

#-------------------------------------------------------------------------------------------------------------------------
# 3. Soma dos números (reduce + lambda)
#  Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].


# from functools import reduce
# lista=[1, 2, 3, 4, 5]
# soma= reduce(lambda x,y: x+y, lista)
# print(soma)



#-------------------------------------------------------------------------------------------------------------------------
# 4. Ordenação por comprimento da palavra (sorted + lambda)
# Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.

# lista = ["uva", "banana", "maçã", "laranja"]

# ordem = sorted(lista, key=lambda x: len(x))
# print(ordem)

#-------------------------------------------------------------------------------------------------------------------------
# 5. Primeira letra maiúscula (map + lambda)
#  Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

# lista= ["ana", "pedro", "maria"]

# nova_lista= list(map(lambda x: x.capitalize(), lista))
# print(nova_lista)

#-------------------------------------------------------------------------------------------------------------------------
# 6. Produto dos números (reduce + lambda)
#  Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].

# from functools import reduce
# lista= [2, 3, 4, 5]
# mult= reduce(lambda x,y: x*y, lista)
# print(mult)


#-------------------------------------------------------------------------------------------------------------------------
# 7. Ordenar por último caractere (sorted + lambda)
# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

# lista =["banana", "uva", "maçã", "laranja"]

# ordena= list(sorted(lista, key=lambda x: x[-1]))
# print(ordena)