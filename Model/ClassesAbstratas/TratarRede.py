from abc import ABC, abstractmethod

class TratarRede(ABC):
    @abstractmethod
    def tratar_rede(self, link: str, pergunta = ''):
        pass

    @abstractmethod
    def remover_Nones(self, array):
        pass