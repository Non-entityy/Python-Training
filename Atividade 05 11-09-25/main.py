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




#---------------------------------------------------------------------------------------------------------------------------------------------------------
#5. Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#6. Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#7. Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#8. Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#9. Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.