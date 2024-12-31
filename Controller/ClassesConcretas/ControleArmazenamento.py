from Model.ClassesAbstratas.Armazenar import Armazenar
from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs

class ControleArmazenamento(ControleArmazenamentoAbs):
    def __init__(self, armazenar: Armazenar):
        super().__init__(armazenar)
        self.__armazenar = armazenar

    def armazenar_dado(self, nome):
        self.__armazenar.armazenar_dado(nome)


    def recuperar_dado(self):
         self.__armazenar.get_dado()

    def imprimir_dados(self):
        print(self.__armazenar.get_dado())