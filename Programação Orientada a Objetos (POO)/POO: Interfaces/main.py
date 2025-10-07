from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def movimentar(self, metros:float):
        ...
class Cachorro(IAnimal):
    def movimentar(self, metros):
        print(f'O cachorro andou {metros} metros.')
dog = Cachorro()
dog.movimentar(5)