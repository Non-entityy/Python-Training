# Atividade: POO - Classes abstratas
from abc import ABC, abstractmethod

# 1. Definição de classe abstrata
# Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. Mostre o uso criando objetos e chamando o método falar().

class Animal(ABC):
    @abstractmethod
    def falar(self, animal):
        print(f'O {animal} está se comunicando.')
class Gato(Animal):
    def falar(self, animal):
        return super().falar(animal)
class Cachorro(Animal):
    def falar(self, animal):
        return super().falar(animal)
dog = Cachorro()
gato = Gato()
gato.falar('gato')
dog.falar('cachorro')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. roibição de instanciamento
# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Múltiplos métodos abstratos
# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Herança parcial
# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

