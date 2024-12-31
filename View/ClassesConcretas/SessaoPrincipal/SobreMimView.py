from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class SobreMim(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                sobreMim = input('Fale sobre você: ')
                self.__tratador.verificar_len_zero(sobreMim)
                self.__armazenar.armazenar_dado({'Sobre mim': sobreMim})
                return self.__armazenar.get_dado()
            except ValueError as e:
                print(e)