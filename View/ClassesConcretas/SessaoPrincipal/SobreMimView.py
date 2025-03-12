from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class SobreMim(Dados):
    def __init__(self, tratador: ControleTratamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                sobreMim = input('Fale sobre você: ')
                self.__tratador.verificar_len_zero(sobreMim)
                self.__dado.append(sobreMim)
                return
            except ValueError as e:
                print(e)

    def get_dado(self):
        return self.__dado
