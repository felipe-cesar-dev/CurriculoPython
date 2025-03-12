from Controller.ClassesAbstratas.ControleTratamentoDataNascAbs import ControleTratamentoDataNascAbs
from View.ClassesAbstratas.Dados import Dados


class DataNascimento(Dados):
    def __init__(self, tratador: ControleTratamentoDataNascAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                dataNasc = input('Digite a data do seu nascimento (DD/MM/AAAA): ')
                self.__tratador.tratar_data_nasc(dataNasc)
                self.__dado.append(dataNasc)
                return
            except ValueError:
                print('Formato Inválido!')

    def get_dado(self):
        return self.__dado

