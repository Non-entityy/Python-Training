#Lista de Exercícios – POO: Herança


# 1. Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

# class Cliente(Usuario):
#     def __str__(self):
#         return f'\nDados do Cliente: \nNome: {self.nome}\nEmail: {self.email}'

# cliente = Cliente('Lucas', 'Lucasp@gmail.com')
# print(cliente)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.

# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

#     def exibir_informacoes(self):
#         return f'\nDados do Cliente \nNome: {self.nome}\nEmail: {self.email}'

# class Cliente(Usuario):
#     pass


# cliente= Cliente('Lucas', 'Lucasp@gmail.com')
# print(cliente.exibir_informacoes())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.

# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

#     def __str__(self):
#         return f'\n|Seus Dados|\nNome: {self.nome}\nEmail: {self.email}'

#     def saudacao(self):
#         return f'Olá, usuário.'
# class Cliente(Usuario):
#     def saudacao(self):
#         return f'Olá, cliente.'
# cliente= Cliente('Lucas', 'Lucasp@gmail.com')
# print(cliente.saudacao())
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().


# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

#     def __str__(self):
#         return f'\n|Seus Dados|\n Nome: {self.nome}\n Email: {self.email}'

# class Cliente(Usuario):
#     def __init__(self, nome, email, saldo):
#         super().__init__(nome, email)
#         self.saldo = saldo
#     def exibir_saldo(self):
#         return f'Saldo: R$ {self.saldo:.2f}'


# cliente= Cliente('Lucas', 'Lucasp@gmail.com', 500)
# print(cliente.exibir_saldo())
# print(cliente)
        


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.

# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

#     def __str__(self):
#         return f'\n|Seus Dados|\n Nome: {self.nome}\n Email: {self.email}'


# class Funcionario(Usuario):
#     pass
# class Gerente(Funcionario):
#     pass
# gerente = Gerente('Lucas', 'lucasp@gmail.com')
# print(gerente.nome)
# print(gerente.email)
# print(gerente)

#OR

# class Usuario:
#     def __init__(self,nome,email):
#         self.nome = nome
#         self.email = email

#     def __str__(self):
#         return f'\n|Seus Dados|\n Nome: {self.nome}\n Email: {self.email}'

# class Funcionario(Usuario):
#     def __init__(self, nome, email, matricula):
#         # Chama o construtor da classe base (Usuario)
#         super().__init__(nome, email)
#         self.matricula = matricula
    
#     def __str__(self):
#         return f"{super().__str__()}\n Matrícula: {self.matricula}"
# class Gerente(Funcionario):
#     def __init__(self, nome, email, matricula, departamento):
#         # Chama o construtor da classe base (Funcionario)
#         super().__init__(nome, email, matricula)
#         self.departamento = departamento
    
#     def __str__(self):
#         return f"{super().__str__()}\n Departamento: {self.departamento}"
# gerente = Gerente(nome="Lucas Peixoto", email="lucasp@empresa.com", matricula="12345", departamento="TI")

#  Acessando atributos
# print(gerente.nome)            # Lucas Peixoto
# print(gerente.email)           # lucasp@empresa.com
# print(gerente.matricula)       # 12345
# print(gerente.departamento)   # TI

#  Usando o método __str__ para imprimir a representação do objeto
# print(gerente)  # Nome: Lucas Peixoto, Email: lucasp@empresa.com, Matrícula: 12345, Departamento: TI

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.

