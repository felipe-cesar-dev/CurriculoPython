from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata

class ControleTratamento(ControleTratamentoAbs):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__(tratador)
        self.__tratador = tratador

    def tratar_dado(self, dado):
        self.__tratador.tratar_palavra(dado)

    def verificar_len_zero(self, dado):
        self.__tratador.verificar_len_zero(dado)