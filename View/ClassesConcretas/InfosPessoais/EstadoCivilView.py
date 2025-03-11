from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class EstadoCivil(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                estadoc = input('Digite seu estado Civil: ')
                self.__tratador.tratar_dado(estadoc)
                self.__controlar.armazenar_dado('dados_unicos', 'estado_civil', estadoc)
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)

