from Model.ClassesAbstratas.Armazenar import Armazenar
from abc import ABC, abstractmethod

class ControleArmazenamentoAbs(ABC):
    def __init__(self, armazenar: Armazenar):
        self.__armazenar = armazenar

    @abstractmethod
    def armazenar_dado(self, nome):
        pass
    @abstractmethod
    def recuperar_dado(self):
         pass
    @abstractmethod
    def imprimir_dados(self):
        pass