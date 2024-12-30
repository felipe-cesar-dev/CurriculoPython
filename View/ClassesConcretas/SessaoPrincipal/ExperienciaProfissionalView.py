from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class ExperienciaProfissional(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__()
        self.__tratador = tratador

    def capturar_dados(self):
        pass