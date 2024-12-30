from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class Nacionalidade(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__()
        self.__tratador = tratador
        self.__nacionalidade = ''

    def capturar_dados(self):
        while True:
            try:
                self.__nacionalidade = input('Digite sua nacionalidade: ')
                self.__tratador.tratar_palavra(self.__nacionalidade)
                return self.__nacionalidade.title()
            except ValueError as e:
                print(e)

    def imprimir_dados(self):
        pass

    def get_dados(self):
        return self.__nacionalidade

