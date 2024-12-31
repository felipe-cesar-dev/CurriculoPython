from Controller.ClassesAbstratas.ControleTratamentoEnderecoAbs import ControleTratamentoEnderecoAbs
from Model.ClassesAbstratas.TratarEndereco import TratarEndereco


class ControleTratamentoEndereco(ControleTratamentoEnderecoAbs):
    def __init__(self, tratador: TratarEndereco):
        super().__init__(tratador)
        self.__tratador = tratador

    def tratar_endereco(self, endereco):
        self.__tratador.tratar_endereco(endereco)
