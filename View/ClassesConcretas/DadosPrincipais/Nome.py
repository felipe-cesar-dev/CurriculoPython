from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class NomeView(Dados):
    def __init__(self, tratador: ControleTratamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dados = []

    def capturar_dados(self):
            while True:
                try:
                    nome = input('Digite seu nome: ')
                    self.__tratador.tratar_dado(nome)
                    #self.__controlar.armazenar_dado('dados_unicos', 'nome', nome)
                    self.__dados.append(nome)
                    break
                except ValueError as e:
                    print(e)


    def get_dados(self):
        return self.__dados






