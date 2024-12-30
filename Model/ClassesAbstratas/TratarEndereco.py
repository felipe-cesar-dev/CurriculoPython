from abc import ABC, abstractmethod

class TratarEndereco(ABC):

    @abstractmethod
    def tratar_endereco(self, endereco):
        pass