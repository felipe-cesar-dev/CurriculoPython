from abc import ABC, abstractmethod
from Model.ClassesAbstratas.TratarCelular import TratarCelular

class ControleTratamentoCelAbs(ABC):
    def __init__(self, tratador: TratarCelular):
        self.__tratador = tratador

    @abstractmethod
    def tratar_celular(self, numero):
        pass
