from Controller.ClassesAbstratas.ControleTratamentoCelAbs import ControleTratamentoCelAbs
from View.ClassesAbstratas.Dados import Dados


class Celular(Dados):
    def __init__(self, tratador: ControleTratamentoCelAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                celular = input('Digite seu celular (11 digitos, somente números): ')
                self.__tratador.tratar_celular(celular)
                self.__dado.append(celular)
                return
            except ValueError as e:
                print(e)

    def get_dado(self):
        return self.__dado





