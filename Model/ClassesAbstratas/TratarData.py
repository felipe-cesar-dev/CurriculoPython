from abc import ABC, abstractmethod

class TratarData(ABC):
    @abstractmethod
    def tratar_data(self, data):
        pass
    @abstractmethod
    def tratar_ano(self, ano):
        pass
    @abstractmethod
    def tratar_mes_ano(self, mesAno):
        pass
