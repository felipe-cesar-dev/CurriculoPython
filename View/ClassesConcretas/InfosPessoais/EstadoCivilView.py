from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class EstadoCivil(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                estadoCivil = input('Digite seu estado civil: ')
                self.__tratador.tratar_palavra(estadoCivil)
                self.__armazenar.armazenar_dado({"Estado Civil": estadoCivil})
                return self.__armazenar.get_dado()
            except ValueError:
                print('Formato Inválido!')