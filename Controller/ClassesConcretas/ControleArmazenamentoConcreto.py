from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Model.ClassesAbstratas.ArmazenamentoGeralAbs import ArmazenamentoGeralAbs


class ControleArmazenamentoConcreto(ControleArmazenamentoAbs):
    def __init__(self, armazenar: ArmazenamentoGeralAbs):
        super().__init__(armazenar)
        self.__armazenar = armazenar

    def armazenar_dado(self, dado):
        self.__armazenar.armazenar_dados_gerais(dado)

    def recuperar_dado(self):
        pass

    def imprimir_dados(self):
        pass