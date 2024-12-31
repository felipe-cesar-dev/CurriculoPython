from Controller.ClassesAbstratas.ControleTratamentoDataNascAbs import ControleTratamentoDataNascAbs
from Model.ClassesAbstratas.TratarData import TratarData


class ControleTratamentoDataNasc(ControleTratamentoDataNascAbs):
    def __init__(self, tratador: TratarData):
        super().__init__(tratador)
        self.__tratador = tratador

    def tratar_data_nasc(self, dataNasc):
        self.__tratador.tratar_data(dataNasc)

    def tratar_mes_ano(self, data):
        self.__tratador.tratar_mes_ano(data)
