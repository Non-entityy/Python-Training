# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self, metros: float):
#         pass
# class Cachorro(Animal):
#     def movimentar(self, metros: float):
#         print(f'O cachorro correu {metros} metros')

# # Testando
# c = Cachorro()
# c.movimentar(10)

#----------------------------------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def comer():
        pass
    @abstractmethod
    def andar():
        pass
    @abstractmethod
    def correr():
        ...