from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Model.ClassesAbstratas.BancodeDadosAbs import BancodeDadosAbs


class ControleArmazenamentoConcreto(ControleArmazenamentoAbs):
    def __init__(self, armazenar: BancodeDadosAbs):
        super().__init__(armazenar)
        self.__armazenar = armazenar

    def armazenar_dado(self, tabela, coluna, dado):
        self.__armazenar.armazenar_dado(tabela, coluna, dado)

    def recuperar_dado(self):
        pass

    def imprimir_dados(self):
        pass