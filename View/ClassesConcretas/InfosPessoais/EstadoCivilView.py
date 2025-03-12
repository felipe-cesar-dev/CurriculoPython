from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class EstadoCivil(Dados):
    def __init__(self, tratador: ControleTratamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dados = []

    def capturar_dados(self):
        while True:
            try:
                estadoc = input('Digite seu estado Civil: ')
                self.__tratador.tratar_dado(estadoc)
                self.__dados.append(estadoc)
                return
            except ValueError as e:
                print(e)

    def get_dados(self):
        return self.__dados

