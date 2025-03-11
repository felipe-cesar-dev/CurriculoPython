from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
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
                    self.__controlar.armazenar_dado('dados_unicos', 'nome', nome)
                    break
                except ValueError as e:
                    print(e)

        if profissao is None:
            while True:
                try:
                    profissao = input('Digite sua profissão: ')
                    self.__tratador.tratar_dado(profissao)
                    self.__controlar.armazenar_dado('dados_unicos', 'profissao', profissao)
                    break
                except ValueError as e:
                    print(e)
        return






