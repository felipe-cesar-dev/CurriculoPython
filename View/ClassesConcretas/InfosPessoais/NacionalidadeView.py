from Controller.ClassesConcretas.ControleTratamento import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class Nacionalidade(Dados):
    def __init__(self, tratador: ControleTratamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                nacionalidade = input('Digite sua nacionalidade: ')
                self.__tratador.tratar_dado(nacionalidade)
                self.__dado.append(nacionalidade)
                return
            except ValueError as e:
                print(e)

    def get_dado(self):
        return self.__dado
