from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoEnderecoAbs import ControleTratamentoEnderecoAbs
from View.ClassesAbstratas.Dados import Dados

class Endereco(Dados):
    def __init__(self, tratador: ControleTratamentoEnderecoAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                endereco = input('Digite seu endereco: ')
                self.__tratador.tratar_endereco(endereco)
                self.__controlar.armazenar_dado({"Endereço" : endereco})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)




