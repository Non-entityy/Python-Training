# Atividade: POO - Classes abstratas
from abc import ABC, abstractmethod

# 1. Definição de classe abstrata
# Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. Mostre o uso criando objetos e chamando o método falar().

# class Animal(ABC):
#     @abstractmethod
#     def falar(self, animal):
#         print(f'O {animal} está se comunicando.')
# class Gato(Animal):
#     def falar(self, animal):
#         return super().falar(animal)
# class Cachorro(Animal):
#     def falar(self, animal):
#         return super().falar(animal)
# dog = Cachorro()
# gato = Gato()
# gato.falar('gato')
# dog.falar('cachorro')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Proibição de instanciamento
# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.


# class Animal(ABC):
#     @abstractmethod
#     def falar(self, animal):
#         print(f'O {animal} está se comunicando.')
# class Gato(Animal):
#     def falar(self, animal):
#         return super().falar(animal)
# class Cachorro(Animal):
#     def falar(self, animal):
#         return super().falar(animal)
# dog = Animal()
# gato = Gato()
# gato.falar('gato')
# dog.falar('cachorro')
#ERRO: TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'falar'

# O @abstractmethod anula qualquer implementação dentro da classe base — ele apenas declara que o método deve existir, mas não pode ser usado diretamente.
# O Python entende que a classe Animal é um modelo incompleto, e que só as subclasses (Gato, Cachorro, etc.) devem implementá-lo e ser instanciadas.
# Mesmo que o método falar() tenha um print dentro dele, ele continua sendo abstrato, porque foi decorado com @abstractmethod.




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Múltiplos métodos abstratos
# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.


# class FormaGeometrica(ABC):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     @abstractmethod
#     def area(self):
#         # Implementação completa do cálculo
#         resultado = self.largura * self.altura
#         print(f"Calculando a área: {self.largura} x {self.altura} = {resultado}")
#         return resultado

#     @abstractmethod
#     def perimetro(self):
#         # Implementação completa do cálculo
#         resultado = 2 * (self.largura + self.altura)
#         print(f"Calculando o perímetro: 2 * ({self.largura} + {self.altura}) = {resultado}")
#         return resultado


# class Retangulo(FormaGeometrica):
#     def __init__(self, largura, altura):
#         super().__init__(largura, altura)

#     def area(self):
#         # Apenas herda o comportamento do pai
#         return super().area()

#     def perimetro(self):
#         # Apenas herda o comportamento do pai
#         return super().perimetro()


# # Teste
# ret = Retangulo(5, 3)
# print(f"Área do retângulo: {ret.area()}")
# print(f"Perímetro do retângulo: {ret.perimetro()}")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Herança parcial
# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

# class Transporte(ABC):
#     @abstractmethod
#     def mover(self):
#         pass

#     @abstractmethod
#     def parar(self):
#         pass


# class Carro(Transporte):
#     def mover(self):
#         print("O carro está se movendo.")
#         # método parar() ainda não foi implementado
        

# # Tentando instanciar
# meu_carro = Carro()
# ERRO: TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'

# Carro herda de Transporte, que tem dois métodos abstratos (mover e parar).
# Como Carro só implementou um deles, ele continua sendo abstrato.
# Por isso, o Python não permite criar um objeto dessa classe.

#CORRIGIDO

# class Transporte(ABC):
#     @abstractmethod
#     def mover(self):
#         pass

#     @abstractmethod
#     def parar(self):
#         pass


# class Carro(Transporte):
#     def mover(self):
#         print("O carro está se movendo.")

#     def parar(self):
#         print("O carro parou.")


# # Agora funciona
# meu_carro = Carro()
# meu_carro.mover()
# meu_carro.parar()