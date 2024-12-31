from Controller.ClassesAbstratas.ControleTratamentoCelAbs import ControleTratamentoCelAbs
from Model.ClassesAbstratas.TratarCelular import TratarCelular


class ControleTratamentoCel(ControleTratamentoCelAbs):
    def __init__(self, tratador: TratarCelular):
        super().__init__(tratador)
        self.__tratador = tratador

    def tratar_celular(self, numero):
        self.__tratador.tratar_celular(numero)