from Model.ClassesAbstratas.TratarRede import TratarRede
from View.ClassesAbstratas.Dados import Dados


class Rede(Dados):
    def __init__(self, tratador: TratarRede):
        super().__init__()
        self._tratador = tratador
        self._rede = ''

    def capturar_dados(self):
        pass


