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

#OR


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self, metros: float):
#         print(f'O cachorro correu {metros} metros')
#         
# class Cachorro(Animal):
#     def movimentar(self, metros: float):
#         return super().movimentar(metros)

# # Testando
# c = Cachorro()
# c.movimentar(10)


#----------------------------------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def comer(self):
        print(f'A pessoa está comendo.')
        pass
    # @abstractmethod
    # def andar(self):
    #     pass
    # @abstractmethod
    # def correr(self):
    #     ...
class Estudante(Pessoa):
    def comer(self):
        return super().comer()
pessoa1= Estudante()
print(pessoa1.comer())