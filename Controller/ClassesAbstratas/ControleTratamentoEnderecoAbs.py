from abc import ABC, abstractmethod
from Model.ClassesAbstratas.TratarEndereco import TratarEndereco


class ControleTratamentoEnderecoAbs(ABC):
    def __init__(self, tratador: TratarEndereco):
        self.__tratador = tratador

    @abstractmethod
    def tratar_endereco(self, endereco):
        pass
