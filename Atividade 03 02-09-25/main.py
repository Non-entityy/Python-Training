#Exercícios de funções

# 1. Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.


# def saudacao():
#      print('Olá, bem-vindo ao Python!')

# saudacao()






#--------------------------------------------------------------------------------------------------------------------------------------------
# 2. Crie uma função chamada dobro que receb um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.


# def dobro(num):
#     return num*2

# print(dobro(2))

#--------------------------------------------------------------------------------------------------------------------------------------------
# 3. Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.

# def soma(num1,num2):
#     return num1+num2
# print(soma(10,20))

#--------------------------------------------------------------------------------------------------------------------------------------------
# 4. Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem: "Olá,[nome]!". Caso o nome não seja informado, mostre "Olá, visitante!".

# def mensagem(nome="visitante"):
#     return f'Olá, {nome}!'
# print(mensagem("Lucas"))
# print(mensagem())

#--------------------------------------------------------------------------------------------------------------------------------------------
# 5. Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

# def operacoes(num1,num2):
#     soma = num1+num2
#     sub = num1-num2
#     mult= num1*num2
#     return soma, sub, mult
# print(operacoes(5,2))


#--------------------------------------------------------------------------------------------------------------------------------------------
# 6. Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

# def media(*numeros):
#     if len(numeros)== 0:
#         return "Nenhum número informado."
#     return sum(numeros)/ len(numeros)
# print(media(10,2,6))
# print(media(4,5,6,3,2))
# print(media(2,3,4,5,6,7,8))

#--------------------------------------------------------------------------------------------------------------------------------------------
# 7. Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada: dados_pessoais(nome="Ana", idade=25, cidade="Recife")

# def dados_pessoais(**kwargs):
#   for chave, valor in kwargs.items():
#      print(f'{chave.capitalize()}: {valor}')
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")


#--------------------------------------------------------------------------------------------------------------------------------------------
# 8. Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.

# def calculadora(operacao, a, b):
#     def somar(x, y):
#         return x + y

#     def subtrair(x, y):
#         return x - y

#     def multiplicar(x, y):
#         return x * y

#     def dividir(x, y):
#         if y == 0:
#             return "Erro: divisão por zero"
#         return x / y

#     if operacao == "somar":
#         return somar(a, b)
#     elif operacao == "subtrair":
#         return subtrair(a, b)
#     elif operacao == "multiplicar":
#         return multiplicar(a, b)
#     elif operacao == "dividir":
#         return dividir(a, b)
#     else:
#         return "Operação inválida"

# print(calculadora("somar", 10, 5))      
# print(calculadora("subtrair", 10, 5))     
# print(calculadora("multiplicar", 10, 5))  
# print(calculadora("dividir", 10, 2))      
# print(calculadora("dividir", 10, 0))      
# print(calculadora("raiz", 9, 3))         

    

#--------------------------------------------------------------------------------------------------------------------------------------------
# 9. Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo: def soma(a, b): return a + b. aplicar_operacao(3, 4, soma)

# def aplicar_operacao(a,b,operacao):
#     return operacao(a,b)
# def soma(a,b):
#      return a + b
# def subtracao(a,b):
#     return a-b
# def multiplicacao(a,b):
#     return a*b
# def divisao(a,b):
#     return a/b

# print(aplicar_operacao(3, 4, soma))
# print(aplicar_operacao(3, 4, subtracao))
# print(aplicar_operacao(3, 4, multiplicacao))
# print(aplicar_operacao(3, 4, divisao))