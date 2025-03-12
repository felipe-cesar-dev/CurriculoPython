from Controller.ClassesAbstratas.ControleTratamentoEmailAbs import ControleTratamentoEmailAbs
from View.ClassesAbstratas.Dados import Dados


class Email(Dados):
    def __init__(self, tratador: ControleTratamentoEmailAbs):
        super().__init__()
        self.__tratador = tratador
        self.__dado = []

    def capturar_dados(self):
        while True:
            try:
                email = input('Digite seu email: ')
                self.__tratador.tratar_email(email)
                self.__dado.append(email)
                return
            except ValueError as e:
                print(e)

    def get_dado(self):
        return self.__dado




