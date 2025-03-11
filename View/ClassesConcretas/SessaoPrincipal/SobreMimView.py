from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoAbs import ControleTratamentoAbs
from View.ClassesAbstratas.Dados import Dados

class SobreMim(Dados):
    def __init__(self, tratador: ControleTratamentoAbs, armazenar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                sobreMim = input('Fale sobre você: ')
                self.__tratador.verificar_len_zero(sobreMim)
                self.__armazenar.armazenar_dado({'Sobre mim': sobreMim})
                return self.__armazenar.imprimir_dados()
            except ValueError as e:
                print(e)