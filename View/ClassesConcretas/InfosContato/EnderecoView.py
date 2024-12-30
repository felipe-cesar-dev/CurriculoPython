from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarEndereco import TratarEndereco
from View.ClassesAbstratas.Dados import Dados


class Endereco(Dados):
    def __init__(self, tratador: TratarEndereco, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                endereco = input('Digite seu endereco: ')
                self.__tratador.tratar_endereco(endereco)
                self.__armazenar.armazenar_dado({"Endereço" : endereco})
                return self.__armazenar.get_dado()
            except ValueError as e:
                print(e)




