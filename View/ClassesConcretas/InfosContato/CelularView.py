from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoCelAbs import ControleTratamentoCelAbs
from View.ClassesAbstratas.Dados import Dados


class Celular(Dados):
    def __init__(self, tratador: ControleTratamentoCelAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                celular = input('Digite seu celular: ')
                self.__tratador.tratar_celular(celular)
                self.__controlar.armazenar_dado({'Celular' : celular})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)





