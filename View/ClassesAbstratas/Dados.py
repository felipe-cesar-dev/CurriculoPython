from abc import ABC, abstractmethod

class Dados(ABC):
    def __init__(self, tratador = ''):
        self.__tratador = tratador
        self.__dados = ''

    @abstractmethod
    def capturar_dados(self):
        pass