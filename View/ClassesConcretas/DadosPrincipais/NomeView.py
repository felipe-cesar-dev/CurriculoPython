from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class Nome(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                nome = input('Digite seu nome: ')
                self.__tratador.tratar_palavra(nome)
                self.__armazenar.armazenar_nome({'Nome': nome})
                return self.__armazenar.get_nome()
            except ValueError as e:
                print(e)