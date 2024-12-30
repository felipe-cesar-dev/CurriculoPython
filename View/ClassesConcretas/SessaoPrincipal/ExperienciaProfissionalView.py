from math import expm1
from multiprocessing.managers import Value

from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarData import TratarData
from View.ClassesAbstratas.Dados import Dados



class ExperienciaProfissional(Dados):
    def __init__(self, tratador: TratarData, armazenar: Armazenar):
        super().__init__()
        self.__armazenar = armazenar
        self.__tratador = tratador

    def capturar_dados(self):
        while True:
            pergunta = input("Deseja adicionar alguma experiência ao currículo? (1 - Sim / 2 - Não) ")
            if pergunta == '1':
                while True:
                    empresa = input("Digite o nome da empresa: ")
                    if len(empresa) == 0:
                        print("Digite algo!")
                    else:
                        while True:
                            inicio = input(f"Digite a data de começo na empresa {empresa.title()} (MM/AAAA): ")
                            if self.__tratador.tratar_mes_ano(inicio):
                                while True:
                                    fim = input(f"Digite a data de saída da empresa {empresa.title()} (MM/AAAA): ")
                                    if self.__tratador.tratar_mes_ano(fim):
                                        self.__armazenar.armazenar_dado({"Empresa" : empresa, "Início" : inicio, "Término" : fim})
                                        return
                                    else: pass
                            else: pass



