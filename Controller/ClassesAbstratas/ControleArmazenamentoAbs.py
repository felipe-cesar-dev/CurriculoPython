from abc import ABC, abstractmethod
from Model.ClassesAbstratas.ArmazenamentoGeralAbs import ArmazenamentoGeralAbs

class ControleArmazenamentoAbs(ABC):
    def __init__(self, armazenar: ArmazenamentoGeralAbs):
        self.__armazenar = armazenar

    @abstractmethod
    def armazenar_dado(self,dado):
        pass
    @abstractmethod
    def recuperar_dado(self):
         pass
    @abstractmethod
    def imprimir_dados(self):
        pass