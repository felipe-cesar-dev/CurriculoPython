from abc import ABC, abstractmethod

class BancodeDadosAbs(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def armazenar_dado(self,tabela, coluna, dado):
        pass