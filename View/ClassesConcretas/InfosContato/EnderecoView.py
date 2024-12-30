from Model.ClassesAbstratas.TratarEndereco import TratarEndereco
from View.ClassesAbstratas.Dados import Dados


class Endereco(Dados):
    def __init__(self, tratador: TratarEndereco):
        super().__init__()
        self.__tratador = tratador
        self.__endereco = ''

    def capturar_dados(self):
        while True:
            try:
                self.__endereco = input('Digite seu endereco: ')
                self.__tratador.tratar_endereco(self.__endereco)
                return self.__endereco.title()
            except ValueError as e:
                print(e)




