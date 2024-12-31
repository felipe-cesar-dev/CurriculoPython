from abc import ABC, abstractmethod
from Model.ClassesAbstratas.TratarData import TratarData



class ControleTratamentoDataNascAbs(ABC):
    def __init__(self, tratador: TratarData):
        self.__tratador = tratador

    @abstractmethod
    def tratar_data_nasc(self, dataNasc):
        pass

    def tratar_mes_ano(self, data):
        pass
