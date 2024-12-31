from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from View.ClassesAbstratas.Dados import Dados


class ConhecimentoseCursos(Dados):
    def __init__(self, armazenar: ControleArmazenamento):
        super().__init__()
        self.__armazenar = armazenar

    def capturar_dados(self):
        while True:
            pergunta = input("Deseja adicionar algum curso ou conhecimento ao seu currículo? (1 - Sim / 2 - Não): ")
            if pergunta == '1':
                self.questionario_cc()
            elif pergunta == '2':
                break
            else:
                print("Digite um número válido!")
            continuar = input("Deseja continuar adicionando? (1 - Sim/ 2 - Não) ")
            if continuar == '1':
                self.questionario_cc()
            elif continuar == '2':
                break
            else:
                print("Digite um número válido")

    def questionario_cc(self):
        while True:
            cc = input("O que deseja adicionar? (0 - Sair)\nEx.: Gestor de empresar - 2000 a 2005 / Conhecimento em Python ")
            if cc == '0':
                break
            elif len(cc) == 0:
                print("Digite algo!")
            else:
                        self.__armazenar.armazenar_dado({"Capacitação" : cc})
                        self.__armazenar.imprimir_dados()
                        return




