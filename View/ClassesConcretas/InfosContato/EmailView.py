from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarEmail import TratarEmail
from View.ClassesAbstratas.Dados import Dados


class Email(Dados):
    def __init__(self, tratador: TratarEmail, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                email = input('Digite seu email: ')
                self.__tratador.tratar_email(email)
                self.__armazenar.armazenar_dado({'Celular' : email})
                return self.__armazenar.get_dado()
            except ValueError as e:
                print(e)





