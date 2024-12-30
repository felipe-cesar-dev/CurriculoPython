from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarRede import TratarRede
from View.ClassesAbstratas.Dados import Dados

class Rede(Dados):
    def __init__(self, tratador: TratarRede, armazenar: Armazenar):
        super().__init__()
        self._tratador = tratador
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            pergunta = input("Deseja adicionar alguma rede social ao seu currículo? (1 - Sim / 2 - Não): ")
            if pergunta == '1':
                self.questionario_rede()
            elif pergunta == '2':
                break
            else: print("Digite um número válido!")
            continuar = input("Deseja continuar adicionando? (1 - Sim/ 2 - Não) ")
            if continuar == '1':
                self.questionario_rede()
            elif continuar == '2':
                break
            else: print("Digite um número válido")

    def questionario_rede(self):
        while True:
            rede = input("Qual rede deseja adicionar? (0 - Sair) ")
            if rede == '0':
                break
            elif len(rede) == 0:
                print("Digite algo!")
            else:
                while True:
                    link = input(f'Digite seu perfil no {rede}: (ex: {rede.lower()}.com/meuperfil) ')
                    if len(link) == 0:
                        print("Digite algo!")
                    else:
                        self.__armazenar.armazenar_dado({"Rede": rede, "Perfil" : link})
                        return




