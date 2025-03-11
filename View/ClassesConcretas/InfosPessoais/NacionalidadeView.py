from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesConcretas.ControleTratamento import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class Nacionalidade(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                nacionalidade = input('Digite sua nacionalidade: ')
                self.__tratador.tratar_dado(nacionalidade)
                self.__controlar.armazenar_dado({'Nacionalidade': nacionalidade})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)