from abc import ABC, abstractmethod

class BancodeDadosAbs(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def armazenar_primary_key(self,nome,tabela, coluna):
        pass
    @abstractmethod
    def update_linha(self, nome, tabela, coluna, dado):
        pass

    def fechar_conexao(self):
        pass