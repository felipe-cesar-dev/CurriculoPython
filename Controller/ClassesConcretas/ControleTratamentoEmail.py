from Controller.ClassesAbstratas.ControleTratamentoEmailAbs import ControleTratamentoEmailAbs
from Model.ClassesAbstratas.TratarEmail import TratarEmail


class ControleTratamentoEmail(ControleTratamentoEmailAbs):
    def __init__(self, tratador: TratarEmail):
        super().__init__(tratador)
        self.__tratador = tratador

    def tratar_email(self, email):
        self.__tratador.tratar_email(email)
