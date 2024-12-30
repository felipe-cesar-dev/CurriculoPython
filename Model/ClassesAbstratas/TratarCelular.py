from abc import ABC, abstractmethod

class TratarCelular(ABC):
    @abstractmethod
    def tratar_celular(self, numero):
        pass