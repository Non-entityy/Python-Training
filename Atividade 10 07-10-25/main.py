# Atividade: POO - Interfaces

# 1. Criando uma interface
# Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.
from abc import ABC, abstractmethod

# class Pagamento(ABC):
#    @abstractmethod
#    def processar(self, valor):
#        pass
# class CartaoCredito(Pagamento):
#    def processar(self, valor):
#        print(f"Processando pagamento de R${valor:.2f} no cartão de crédito.")

# class Boleto(Pagamento):
#    def processar(self, valor):
#        print(f"Processando pagamento de R${valor:.2f} via boleto bancário.")

# Criando objetos
# pagamento_cartao = CartaoCredito()
# pagamento_boleto = Boleto()

# Chamando o método processar()
# pagamento_cartao.processar(150.00)
# pagamento_boleto.processar(89.90)




# 2. Interface múltipla
# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.


# class Ligavel(ABC):
#    @abstractmethod
#    def ligar(self):
#        pass

# class Desligavel(ABC):
#    @abstractmethod
#    def desligar(self):
#        pass
# class Computador(Ligavel, Desligavel):
#    def ligar(self):
#        print("Computador ligado.")

#    def desligar(self):
#        print("Computador desligado.")
# Criando objeto
# pc = Computador()

# Chamando os métodos
# pc.ligar()
# pc.desligar()




# 3. Interface em herança múltipla
# Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

# class Imprimivel(ABC):
#    @abstractmethod
#    def imprimir(self):
#        pass

# class Exportavel(ABC):
#    @abstractmethod
#    def exportar(self):
#        pass
# class Relatorio(Imprimivel, Exportavel):
#    def imprimir(self):
#        print("Imprimindo relatório em papel...")

#    def exportar(self):
#        print("Exportando relatório em PDF...")
# Criando objeto
# rel = Relatorio()

# Chamando os métodos
# rel.imprimir()
# rel.exportar()

# 4. Forçando contrato
# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.



# class Repositorio(ABC):
#    @abstractmethod
#    def salvar(self, objeto):
#        pass

#    @abstractmethod
#    def buscar(self, id):
#        pass
# class RepositorioMemoria(Repositorio):
#    def salvar(self, objeto):
#        print("Objeto salvo em memória.")
# repo = RepositorioMemoria()

# ERRO: TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract method 'buscar'
# O Python impede a criação da instância porque a classe não implementou todos os métodos obrigatórios da interface.
# CORREÇÂO:


# class Repositorio(ABC):
#    @abstractmethod
#    def salvar(self, objeto):
#        pass

#    @abstractmethod
#    def buscar(self, id):
#        pass
# class RepositorioMemoria(Repositorio):
#    def __init__(self):
#        self._dados = {}
#        self._proximo_id = 1

#    def salvar(self, objeto):
#        self._dados[self._proximo_id] = objeto
#        print(f"Objeto salvo com ID {self._proximo_id}")
#        self._proximo_id += 1

#    def buscar(self, id):
#       return self._dados.get(id, "Objeto não encontrado.")

# repo = RepositorioMemoria()
# repo.salvar("Relatório 1")
# repo.salvar("Relatório 2")

# print(repo.buscar(1))  
# print(repo.buscar(99))