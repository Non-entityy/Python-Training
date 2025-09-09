# Exercícios sobre exceptions

# 1. Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.


#while true:
# try:
#    x = int(input('Digite um número inteiro: '))
# except ValueError:
#     print(f'Você não digitou um número inteiro.')
# else:
#     print(f'Você digitou um número inteiro: {x}')
#     break
#OR
# try:
#    x = int(input('Digite um número inteiro: '))
#    print(f'O número que você digitou é: {x}')
# except ValueError:
#     print(f'Você não digitou um número inteiro.')





#------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

# try:
#     print('Digite dois números inteiros para multiplicalos:')
#     print('')
#     x = int(input('Digite o primeiro número inteiro: '))
#     y = int(input('Digite o segundo número inteiro: '))
#     resultado = x*y
# except ValueError:
#     print('Erro: Você deve digitar um número válido. ')
# else:
#     print(f'O resultado é: {resultado}')


#------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

# try:
#     x = int(input('Digite um número inteiro: '))
# except ValueError:
#     print('Erro: Digite um número inteiro.')
# else:
#     print(f'Você digitou o número: {x}')



#------------------------------------------------------------------------------------------------------------------------------------------------
# 4.Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

# try:
#     with open('dados.txt', 'r') as f:
#         conteudo = f.read()
# except FileNotFoundError:
#     print('Arquivo não encontrado.')
# finally:
#     print('Encerrando programa')


#------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

# def dividir(a, b):
#   if b == 0:
#     raise ZeroDivisionError('Divisão por zero não é permitida')
#   return a/b
# try:
#   resultado = dividir(2,0)
#   print(f'A divisão é: {resultado}')
# except ZeroDivisionError as erro: 
#   print(f'Error: {erro}')

    

#------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

# class idadeInvalidaError(Exception):
#     def __init__(self, idade, mensagem='A idade não pode ser negativa.'):
#         self.idade = idade
#         self.mensagem = mensagem
#         super().__init__(self.mensagem)
# def cadastrar_idade(idade):
#     if idade < 0:
#         raise idadeInvalidaError(idade)
#     else:
#         print(f'Idade cadastrada com sucesso: {idade} anos')
# try:
#     cadastrar_idade(5)
# except idadeInvalidaError as e:
#     print(f'Erro: {e.mensagem} Idade fornecida: {e.idade}')


#------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro: ValueError se o usuário digitar algo inválido | ZeroDivisionError se tentar dividir por zero

# def dividir_numeros():
#     try:
#         x = float(input('Digite o primeiro número: '))
#         y = float(input('Digite o segundo número: '))
#         resultado = x/y
#         print(f'O resultado da divisão é: {resultado}')
#     except ZeroDivisionError:
#         print('Erro: Não é possível dividir por 0.')
#     except ValueError:
#         print('Erro: Digite números válidos.')
#     except Exception as e:
#         print(f'Erro inesperado: {e}')

# dividir_numeros()




#------------------------------------------------------------------------------------------------------------------------------------------------
# 8. Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use: try para a conversão, else para verificar se é par ou ímpar, finally para exibir "Fim do programa".

# x = input('Digite um número inteiro: ')
# try:
#     x = int(x)
# except ValueError as e:
#     print(f'Error: {e}')
# else:
#     if x%2 == 0:
#         print(f'O número {x} é par.')
#     else:
#         print(f'O número {x} é ímpar.')
# finally:
#     print('Fim do programa.')
    

#------------------------------------------------------------------------------------------------------------------------------------------------
# 9. Crie uma função sacar(saldo, valor) que: Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo. Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.

# class SaldoInsuficienteError(Exception):
#     def __init__(self, mensagem):
#         super().__init__(mensagem)

# def sacar(saldo, valor):
#     if saldo < valor:
#         raise SaldoInsuficienteError(f'Seu saldo é insuficiente: {saldo} R$')
#     return saldo-valor
# try:
#     saldo_atual = 80
#     valor_saque = 20
#     resultado = sacar(saldo_atual,valor_saque)
#     print(f'Valor anterior: {saldo_atual} R$')
#     print(f'Retirado com sucesso! Novo saldo: {resultado} R$')
# except SaldoInsuficienteError as e:
#     print(f'Erro: {e}')