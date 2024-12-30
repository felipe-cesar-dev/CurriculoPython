from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarCelular import TratarCelular
from View.ClassesAbstratas.Dados import Dados


class Celular(Dados):
    def __init__(self, tratador: TratarCelular, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                celular = input('Digite seu celular: ')
                self.__tratador.tratar_celular(celular)
                self.__armazenar.armazenar_dado({'Celular' : celular})
                return self.__armazenar.get_dado()
            except ValueError as e:
                print(e)





