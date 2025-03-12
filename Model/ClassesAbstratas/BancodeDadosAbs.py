from abc import ABC, abstractmethod

class BancodeDadosAbs(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def armazenar_dado(self,nome,tabela, coluna, dado):
        pass