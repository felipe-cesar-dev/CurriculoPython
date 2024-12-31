from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesAbstratas.ControleTratamentoEmailAbs import ControleTratamentoEmailAbs
from Model.ClassesAbstratas.TratarEmail import TratarEmail
from View.ClassesAbstratas.Dados import Dados


class Email(Dados):
    def __init__(self, tratador: ControleTratamentoEmailAbs, controlar: ControleArmazenamentoAbs):
        super().__init__()
        self.__tratador = tratador
        self.__controlar = controlar

    def capturar_dados(self):
        while True:
            try:
                email = input('Digite seu email: ')
                self.__tratador.tratar_email(email)
                self.__controlar.armazenar_dado({'E-mail' : email})
                return self.__controlar.imprimir_dados()
            except ValueError as e:
                print(e)





