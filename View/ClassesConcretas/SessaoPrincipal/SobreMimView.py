from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from View.ClassesAbstratas.Dados import Dados


class SobreMim(Dados):
    def __init__(self, tratador: TratarpalavraAbstrata):
        super().__init__()
        self.__tratador = tratador
        self.__sobreMim = ''

    def capturar_dados(self):
        while True:
            try:
                self.__sobreMim = input('Esceva um pouco sobre si: ')
                self.__tratador.verificar_len_zero(self.__sobreMim)
                return self.__sobreMim
            except ValueError as e:
                print(e)
