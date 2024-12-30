from Model.ClassesAbstratas.TratarEmail import TratarEmail
from View.ClassesAbstratas.Dados import Dados


class Email(Dados):
    def __init__(self, tratador: TratarEmail):
        super().__init__()
        self.__tratador = tratador
        self.__email = ''

    def capturar_dados(self):
        while True:
            try:
                self.__email = input('Digite seu email: ')
                self.__tratador.tratar_email(self.__email)
                return self.__email
            except ValueError as e:
                print(e)





