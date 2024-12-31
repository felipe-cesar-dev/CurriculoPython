from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados


class Profissao(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                profissao = input('Digite seu profissão: ')
                self.__tratador.tratar_palavra(profissao)
                self.__controlar.armazenar_dado({'Profissão': profissao})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)