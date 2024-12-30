from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class Profissao(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__()
        self.__tratador = tratador
        self.__profissao = ''

    def capturar_dados(self):
        while True:
            try:
                self.__profissao = input('Digite sua profissão: ')
                self.__tratador.tratar_palavra(self.__profissao)
                return self.__profissao.title()
            except ValueError as e:
                print(e)