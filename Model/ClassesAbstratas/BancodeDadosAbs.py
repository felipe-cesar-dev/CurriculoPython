from abc import ABC, abstractmethod

class BancodeDadosAbs(ABC):
    def __init__(self):
        self.__dado = []

    @abstractmethod
    def conectar(self, nome_do_banco):
        pass

    @abstractmethod
    def armazenar_dado(self, tabela, coluna, dado):
        pass

    @abstractmethod
    def fechar_conexao(self):
        pass