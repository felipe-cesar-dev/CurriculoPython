from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarData import TratarData
from View.ClassesAbstratas.Dados import Dados


class DataNascimento(Dados):
    def __init__(self, tratador: TratarData, armazenar: Armazenar):
        super().__init__()
        self.__tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            try:
                dataNasc = input('Digite a data do seu nascimento (DD/MM/AAAA): ')
                self.__tratador.tratar_data(dataNasc)
                self.__armazenar.armazenar_dado({"Data de Nascimento": dataNasc})
                return self.__armazenar.get_dado()
            except ValueError:
                print('Formato Inválido!')

