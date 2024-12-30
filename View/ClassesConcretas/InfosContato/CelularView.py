from Model.ClassesAbstratas.TratarCelular import TratarCelular
from View.ClassesAbstratas.Dados import Dados


class Celular(Dados):
    def __init__(self, tratador: TratarCelular):
        super().__init__()
        self.__tratador = tratador
        self.__celular = int

    def capturar_dados(self):
        while True:
            try:
                self.__celular = input('Digite seu celular: ')
                self.__tratador.tratar_celular(self.__celular)
                return self.__celular
            except ValueError as e:
                print(e)





