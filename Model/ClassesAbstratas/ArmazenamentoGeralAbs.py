from abc import ABC, abstractmethod

class ArmazenamentoGeralAbs(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def armazenar_dados_gerais(self, dado):
        pass

    @abstractmethod
    def get_dados_gerais(self):
        pass