# 1. Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = 0
#         self.set_saldo(saldo)
#     def __str__(self):
#         return f'Nome: {self.titular} | Saldo: {self.__saldo}'
#     def get_saldo(self):
#         return self.__saldo
#     def set_saldo(self, valor):
#         if valor >=0:
#             self.__saldo = valor
#         else:
#             print("Erro: O saldo não pode ser negativo.")
# conta = ContaBancaria('Lucas', 100)
# print(conta)
# conta.set_saldo(500)
# print(conta)
# conta.set_saldo(-10)
# print(conta)




# 2. Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores


