from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from abc import ABC, abstractmethod

class ControleTratamentoAbs(ABC):
    def __init__(self, tratador: TratarpalavraAbstrata):
        self.__tratador = tratador

    @abstractmethod
    def tratar_dado(self, dado):
        pass

    @abstractmethod
    def verificar_len_zero(self, dado):
        pass