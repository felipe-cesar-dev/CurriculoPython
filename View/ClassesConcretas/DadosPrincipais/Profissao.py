from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class Profissao(Dados):
    def __init__(self, tratador: ControleTratamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dados = []

    def capturar_dados(self):
            while True:
                try:
                    profissao = input('Digite sua profissão: ')
                    self.__tratador.tratar_dado(profissao)
                    #self.__controlar.armazenar_dado('dados_unicos', 'profissao', profissao)
                    self.__dados.append(profissao)
                    break
                except ValueError as e:
                    print(e)

    def get_dados(self):
        return self.__dados






