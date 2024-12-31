from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoDataNascAbs import ControleTratamentoDataNascAbs
from View.ClassesAbstratas.Dados import Dados


class DataNascimento(Dados):
    def __init__(self, tratador: ControleTratamentoDataNascAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                dataNasc = input('Digite a data do seu nascimento (DD/MM/AAAA): ')
                self.__tratador.tratar_data_nasc(dataNasc)
                self.__controlar.armazenar_dado({"Data de Nascimento": dataNasc})
                return self.__controlar.imprimir_dados()
            except ValueError:
                print('Formato Inválido!')

