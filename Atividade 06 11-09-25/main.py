# POO - Encapsulamento

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



#-------------------------------------------------------------------------------------------------------------------------
# 2. Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores

# class Pessoa:
#     def __init__(self, nome, data, cpf, identidade):
#         self.nome = nome
#         self.data = data
#         self.__cpf = self.validar(cpf)
#         self.__identidade = identidade
#     def __str__(self):
#         return f'Nome: {self.nome} | Data de nascimento: {self.data}'
#     def get_cpf(self):
#         return self.__cpf
#     def set_cpf(self, cpf):
#         self.__cpf = self.validar(cpf)
#     def get_identidade(self):
#         return self.__identidade
#     def set_identidade(self, identidade):
#         self.__identidade = identidade
#     def validar(self, cpf):
#         cpf_str = str(cpf)
#         # Validação simplificada (apenas checa o formato de 11 dígitos)
#         if len(cpf_str) == 11 and cpf_str.isdigit():
#             return cpf_str
#         else:
#             raise ValueError("CPF inválido. Deve conter 11 dígitos.")
# pessoa = Pessoa('Lucas', '27/11/1997', 14736512413, 11560789)
# print(pessoa)
# print(f'CPF antes: {pessoa.get_cpf()}')
# pessoa.set_cpf(12345678912)
# print(f'CPF depois: {pessoa.get_cpf()}')
      
