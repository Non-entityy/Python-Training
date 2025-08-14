#Objetivo: Entender como criar e reutilizar código.
#1. Função de saudação
# def saudar():
#   return f'Óla, {nome}.'
# nome = input("Digite seu nome: ")
# print("")
# resultado = saudar()
# print(resultado)
#Or
#
#---------------------------------------------------------------------------------
#2. Calculadora simples
# def soma(a, b):
#     return f'A soma é: {a + b}'
# def sub(a, b):
#     return f'A subtração é: {a - b}'
# def mult(a, b):
#     return f'A multiplicação é: {a * b}'
# def div(a, b):
#     if b == 0:
#         return "Erro: divisão por zero."
#     return f'A divisão é: {a / b}'
# x = float(input("Digite o primeiro número: "))
# y = float(input("Digite o segundo número: "))
# print("---------------------------------------------")
# print("Para somar digite '+'")
# print("Para subtrair digite '-'")
# print("Para multiplicar digite '*'")
# print("Para dividir digite '/'")
# z = input("Qual operação quer realizar?")
# print("---------------------------------------------")

# if z == "+":
#     print(soma(x, y))
# elif z == "-":
#     print(sub(x, y))
# elif z == "*":
#     print(mult(x, y))
# elif z == "/":
#     print(div(x, y))
# else:
#     print("Operação inválida. Tente novamente.")
#Or
# def soma(a, b):
#     return f'A soma é: {a + b}'

# def sub(a, b):
#     return f'A subtração é: {a - b}'

# def mult(a, b):
#     return f'A multiplicação é: {a * b}'

# def div(a, b):
#     if b == 0:
#         return "Erro: Divisão por zero."
#     return f'A divisão é: {a / b}'

# # Início do loop
# while True:
#     print("\n---------------------------------------------")
#     print("CALCULADORA:")
#     print("Para somar digite '+'")
#     print("Para subtrair digite '-'")
#     print("Para multiplicar digite '*'")
#     print("Para dividir digite '/'")
#     print("Para sair digite 'sair'")
#     print("---------------------------------------------")

#     z = input("Qual operação quer realizar? ").strip()

#     if z.lower() == 'sair':
#         print("Encerrando a calculadora. Até logo!")
#         break

#     # Pede os números só se a operação for válida
#     if z in ['+', '-', '*', '/']:
#         try:
#             x = float(input("Digite o primeiro número: "))
#             y = float(input("Digite o segundo número: "))
#         except ValueError:
#             print("Erro: Digite apenas números válidos.")
#             continue

#         if z == "+":
#             print(soma(x, y))
#         elif z == "-":
#             print(sub(x, y))
#         elif z == "*":
#             print(mult(x, y))
#         elif z == "/":
#             print(div(x, y))
#     else:
#         print("Operação inválida. Tente novamente.")
#OR
operacoes = {
    '+': lambda a, b: f'A soma é: {a + b}',
    '-': lambda a, b: f'A subtração é: {a - b}',
    '*': lambda a, b: f'A multiplicação é: {a * b}',
    '/': lambda a, b: f'A divisão é: {a / b}' if b != 0 else 'Erro: divisão por zero.'
}

while True:
    op = input("\nDigite uma operação (+, -, *, /) ou 'sair': ").strip()
    if op.lower() == 'sair':
        print("Encerrando a calculadora.")
        break
    if op in operacoes:
        try:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print(operacoes[op](a, b))
        except ValueError:
            print("Erro: Digite números válidos.")
    else:
        print("Operação inválida.")
