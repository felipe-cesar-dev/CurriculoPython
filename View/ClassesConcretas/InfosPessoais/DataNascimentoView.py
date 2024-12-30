from Model.ClassesAbstratas.TratarData import TratarData
from View.ClassesAbstratas.Dados import Dados


class DataNascimento(Dados):
    def __init__(self, tratador: TratarData):
        super().__init__()
        self.__dataNasc = ''
        self.__tratador = tratador

    def capturar_dados(self):
        while True:
            try:
                self.__dataNasc = input('Digite a data do seu nascimento (DD/MM/AAAA): ')
                self.__tratador.tratar_data(self.__dataNasc)
                return self.__dataNasc
            except ValueError:
                print('Formato Inválido!')

    def imprimir_dados(self):
        print(self.__dataNasc)

    def get_dados(self):
        return self.__dataNasc
