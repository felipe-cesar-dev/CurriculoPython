from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoEnderecoAbs import ControleTratamentoEnderecoAbs
from View.ClassesAbstratas.Dados import Dados

class Endereco(Dados):
    def __init__(self, tratador: ControleTratamentoEnderecoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                endereco = input('Digite seu endereco: ')
                self.__tratador.tratar_endereco(endereco)
                self.__dado.append(endereco)
                return
            except ValueError as e:
                print(e)

    def get_dado(self):
        return self.__dado




