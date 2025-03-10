from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamentoAbs
from Controller.ClassesConcretas.ControleTratamento import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class NomeView(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self, nome=None, profissao=None):
        if nome is None:
            while True:
                try:
                    nome = input('Digite seu nome: ')
                    self.__tratador.tratar_dado(nome)
                    break
                except ValueError as e:
                    print(e)

        if profissao is None:
            while True:
                try:
                    profissao = input('Digite sua profissão: ')
                    self.__tratador.tratar_dado(profissao)
                    break
                except ValueError as e:
                    print(e)

        self.__controlar.armazenar_dado({'Nome': nome, 'Profissão': profissao})
        return self.__controlar.imprimir_dados()
