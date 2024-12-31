from abc import ABC, abstractmethod
from Model.ClassesAbstratas.TratarEmail import TratarEmail


class ControleTratamentoEmailAbs(ABC):
    def __init__(self, tratador: TratarEmail):
        self.__tratador = tratador

    @abstractmethod
    def tratar_email(self, email):
        pass
