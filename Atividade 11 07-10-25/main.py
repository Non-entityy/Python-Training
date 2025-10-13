# Atividade: POO - Associação / Agregação / Composição



# 1. Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

# class Livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor

#     def __str__(self):
#         return f"'{self.titulo}' de {self.autor}"
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#         self.livros = []  # Lista de livros associados

#     def adicionar_livro(self, livro):
#         self.livros.append(livro)

#     def listar_livros(self):
#         if not self.livros:
#             print(f"{self.nome} não possui livros.")
#         else:
#             print(f"Livros de {self.nome}:")
#             for livro in self.livros:
#                 print(f"  - {livro}")
# # Criando livros
# livro1 = Livro("1984", "George Orwell")
# livro2 = Livro("Dom Casmurro", "Machado de Assis")

# # Criando uma pessoa
# pessoa = Pessoa("João")

# # Associando livros à pessoa
# pessoa.adicionar_livro(livro1)
# pessoa.adicionar_livro(livro2)

# # Mostrando os livros da pessoa
# pessoa.listar_livros()


#---------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

# class Onibus:
#     def __init__(self, numero, destino):
#         self.numero = numero
#         self.destino = destino

#     def __str__(self):
#         return f"Ônibus {self.numero} com destino a {self.destino}"
# class Aluno:
#     def __init__(self, nome):
#         self.nome = nome

#     def pegar_onibus(self, onibus):
#         print(f"{self.nome} está pegando o {onibus}")
# # Criando um ônibus
# onibus_escolar = Onibus(42, "Escola Municipal")

# # Criando um aluno
# aluno1 = Aluno("Carlos")

# # Aluno usa o ônibus
# aluno1.pegar_onibus(onibus_escolar)




#---------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.

# class Funcionario:
#     def __init__(self, nome, cargo):
#         self.nome = nome
#         self.cargo = cargo

#     def __str__(self):
#         return f"{self.nome} ({self.cargo})"
# class Departamento:
#     def __init__(self, nome):
#         self.nome = nome
#         self.funcionarios = []  # Lista agregada

#     def adicionar_funcionario(self, funcionario):
#         self.funcionarios.append(funcionario)

#     def listar_funcionarios(self):
#         print(f"Departamento: {self.nome}")
#         if not self.funcionarios:
#             print("Nenhum funcionário.")
#         else:
#             print("Funcionários:")
#             for f in self.funcionarios:
#                 print(f" - {f}")
# # Criando funcionários (independentes)
# f1 = Funcionario("Ana", "Analista")
# f2 = Funcionario("Carlos", "Desenvolvedor")
# f3 = Funcionario("Lúcia", "Designer")

# # Criando o departamento
# departamento_ti = Departamento("Tecnologia da Informação")

# # Agregando funcionários já criados
# departamento_ti.adicionar_funcionario(f1)
# departamento_ti.adicionar_funcionario(f2)

# # Outro departamento agregando o mesmo funcionário (exemplo de independência)
# departamento_design = Departamento("Design")
# departamento_design.adicionar_funcionario(f3)
# departamento_design.adicionar_funcionario(f2)  # Carlos em dois departamentos

# # Listando funcionários por departamento
# departamento_ti.listar_funcionarios()
# print()
# departamento_design.listar_funcionarios()




#---------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

# class Jogador:
#     def __init__(self, nome, posicao):
#         self.nome = nome
#         self.posicao = posicao

#     def __str__(self):
#         return f"{self.nome} - {self.posicao}"
# class Time:
#     def __init__(self, nome):
#         self.nome = nome
#         self.jogadores = []  # Lista de jogadores agregados

#     def adicionar_jogador(self, jogador):
#         self.jogadores.append(jogador)

#     def listar_jogadores(self):
#         print(f"Time: {self.nome}")
#         if not self.jogadores:
#             print("Nenhum jogador no time.")
#         else:
#             print("Jogadores:")
#             for j in self.jogadores:
#                 print(f" - {j}")
# # Criando jogadores (fora do time)
# j1 = Jogador("Lucas", "Atacante")
# j2 = Jogador("Marcos", "Goleiro")
# j3 = Jogador("João", "Zagueiro")

# # Criando o time
# time_azul = Time("Azul FC")

# # Adicionando jogadores ao time
# time_azul.adicionar_jogador(j1)
# time_azul.adicionar_jogador(j2)
# time_azul.adicionar_jogador(j3)

# # Listando os jogadores do time
# time_azul.listar_jogadores()


#---------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

# class Motor:
#     def __init__(self, potencia):
#         self.potencia = potencia
#         print(f"Motor de {self.potencia}cv criado.")

#     def __del__(self):
#         print(f"Motor de {self.potencia}cv destruído.")

# class Carro:
#     def __init__(self, modelo, potencia_motor):
#         self.modelo = modelo
#         self.motor = Motor(potencia_motor)
#         print(f"Carro {self.modelo} criado.")

#     def __del__(self):
#         print(f"Carro {self.modelo} destruído.")
# # Criando o carro (e seu motor)
# carro = Carro("Fusca", 130)

# # Apagando o carro (o motor também será destruído)
# del carro


#---------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.

# class Comodo:
#     def __init__(self, nome):
#         self.nome = nome
#         print(f"Cômodo '{self.nome}' criado.")

#     def __del__(self):
#         print(f"Cômodo '{self.nome}' destruído.")
# class Casa:
#     def __init__(self, endereco):
#         self.endereco = endereco
#         print(f"Casa no endereço '{self.endereco}' criada.")

#         # Composição: cômodos criados dentro da Casa
#         self.comodos = [
#             Comodo("Sala"),
#             Comodo("Cozinha"),
#             Comodo("Quarto"),
#             Comodo("Banheiro")
#         ]

#     def listar_comodos(self):
#         print(f"Casa em '{self.endereco}' possui os cômodos:")
#         for c in self.comodos:
#             print(f" - {c.nome}")

#     def __del__(self):
#         print(f"Casa no endereço '{self.endereco}' destruída.")
# # Criando a casa (e seus cômodos)
# casa = Casa("Rua das Flores, 123")

# # Listando os cômodos
# casa.listar_comodos()

# # Apagando a casa (os cômodos também serão destruídos)
# del casa


