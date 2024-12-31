from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class Profissao(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                profissao = input('Digite seu profissão: ')
                self.__tratador.tratar_palavra(profissao)
                self.__armazenar.armazenar_dado({'Profissão': profissao})
                return self.__armazenar.get_dado()
            except ValueError as e:
                print(e)