#1. Contagem crescente
# x = 0
# for x in range(1,11):
#     print (x)
#OR
# num= [1,2,3,4,5,6,7,8,9,10]
# for numeros in num:
#     print(numeros)
#OR
# numeros_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for numero in numeros_tupla:
#     print(numero)
#-----------------------------------------------------------------------------
#2. Tabuada
x = int(input("Informe um número: "))
y = [1,2,3,4,5,6,7,8,9,10]
resultados = []
for elemento in y:
    resultados.append(x * elemento)
for resultado in resultados:
    print(resultado)