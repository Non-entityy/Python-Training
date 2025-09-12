# Lista de Exercícios – POO classes e objetos

#1. Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

# class pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
# pessoa1 = pessoa('Lucas', 27)
# pessoa2 = pessoa('Ana', 23)

# print(f'Pessoa1 - Nome: {pessoa1.nome}, Idade: {pessoa1.idade} anos')
# print(f'Pessoa2 - Nome: {pessoa2.nome}, Idade: {pessoa2.idade} anos')


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#2. Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

# class pessoa:
#     def __init__(self, nome, idade):
#          self.nome = nome
#          self.idade = idade
#     def apresentar(self):
#          print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')
# pessoa1 = pessoa('João', 25)

# pessoa1.apresentar()
# #OR
# pessoa.apresentar(pessoa1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#3. Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

# class carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

# carro1 = carro('Hyundai','IONIQ 5', 2025)
# carro2 = carro('Ford','Mustang', 1967)
# carro3 = carro('Chevrolet','Impala', 1958)

# print(f'Carro1 - Marca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}')
# print(f'Carro2 - Marca: {carro2.marca}, Modelo: {carro2.modelo}, Ano: {carro2.ano}')
# print(f'Carro3 - Marca: {carro3.marca}, Modelo: {carro3.modelo}, Ano: {carro3.ano}')
    


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#4. Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

# Usando __STR__ para representar o objeto como string, meio que "converter o objeto em texto legivel" para não precisar acessar manualmente seus atributos.
# class carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def __str__(self):
#         return f'Carro 1º - Marca: {self.marca} | Modelo: {self.modelo} | Ano: ({self.ano})'
# carro1 = carro('Hyundai', 'IONIQ 5', 2024)
# print(carro1)

# carro1.ano = 2025
# print(carro1)

#OR acessa manualmente os atributos

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

# # Criando o objeto
# carro1 = Carro('Hyundai', 'IONIQ 5', 2024)

# # Tentando imprimir o objeto diretamente
# print("Tentando imprimir o objeto direto:")
# print(carro1)

# # Mostrando as informações acessando os atributos manualmente
# print("\nMostrando os dados manualmente:")
# print("Marca:", carro1.marca)
# print("Modelo:", carro1.modelo)
# print("Ano:", carro1.ano)

#OR
# print(vars(carro1)) <- imprime como lista

#OR Criamos uma função para chamar o objeto.

# def mostrar_info(carro):
#     print(f"Marca: {carro.marca}")
#     print(f"Modelo: {carro.modelo}")
#     print(f"Ano: {carro.ano}")

# mostrar_info(carro1)


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#5. Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.


# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#     def __str__(self):
#         return f'Titular: {self.titular} | Saldo: {self.saldo} R$'
#     def depositar(self,valor):
#         self.saldo += valor

#     def sacar(self,valor):
#         if self.saldo < valor or self.saldo <= 0:
#             print('Saldo insuficiente.')
#         else:
#             self.saldo -= valor
# saldo = ContaBancaria('Lucas', 0)
# print(saldo)  
# saldo.depositar(300)  
# print(saldo)    
# saldo.sacar(100)
# print(saldo)
# saldo.sacar(201)
# print(saldo)
# saldo.depositar(1)
# print(saldo)
# saldo.sacar(201)
# print(saldo)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#6. Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#     def __str__(self):
#         return f'Titular: {self.titular} | Saldo: {self.saldo} R$'
#     def depositar(self,valor):
#         self.saldo += valor

#     def sacar(self,valor):
#         if self.saldo < valor or self.saldo <= 0:
#             return False
#         else:
#             self.saldo -= valor
#             return True
# conta = ContaBancaria('Lucas', 50)
# valor = 100
# valor2 = 30
# if conta.sacar(valor):
#     print(f'Tentando sacar: {valor} R$')
#     print(f'Saque realizado: {valor} R$')
# else:
#     print(f'Tentando sacar: {valor} R$')
#     print(f'Saldo insuficiente - Saldo: {conta.saldo} R$')

# if conta.sacar(valor2):
#     print(f'Tentando sacar: {valor2} R$')
#     print(f'Saque realizado: {valor2} R$')
# else:
#      print(f'Tentando sacar: {valor2} R$')
#      print(f'Saldo insuficiente - Saldo: {conta.saldo} R$')
# print('\nSaldo Final:')
# print(conta)


#OR acessando diretamente o TRUE OR FALSE do objeto com IF
# print(conta)
# if conta.sacar(100):
#     print(f'Saque realizado: {100} R$')
# else:
#     print(f'Saldo insuficiente.')
# print(conta)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#7. Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
class Turma:
    lista_alunos = []
        

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#8. Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#9. Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.