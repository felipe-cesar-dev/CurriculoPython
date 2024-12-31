from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamentoAbs
from Controller.ClassesConcretas.ControleTratamento import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class NomeView(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                nome = input('Digite seu nome: ')
                self.__tratador.tratar_palavra(nome)
                self.__controlar.armazenar_dado({'Nome': nome})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)