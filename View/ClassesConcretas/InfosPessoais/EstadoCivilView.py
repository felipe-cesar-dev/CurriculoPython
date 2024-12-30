from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class EstadoCivil(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__()
        self.__tratador = tratador
        self.__estadoCivil = ''

    def capturar_dados(self):
        while True:
            try:
                self.__estadoCivil = input('Digite seu estado civil: ')
                self.__tratador.tratar_palavra(self.__estadoCivil)
                return self.__estadoCivil.title()
            except ValueError as e:
                print(e)
