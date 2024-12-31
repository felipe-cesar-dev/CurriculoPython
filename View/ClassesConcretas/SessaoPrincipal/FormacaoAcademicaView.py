from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesAbstratas.TratarData import TratarData
from View.ClassesAbstratas.Dados import Dados


class FromacaoAcademica(Dados):
    def __init__(self, tratador: TratarData, armazenar: Armazenar):
        super().__init__()
        self.__armazenar = armazenar
        self.__tratador = tratador

    def capturar_dados(self):
        while True:
            pergunta = input("Deseja adicionar alguma formação ao currículo? (1 - Sim / 2 - Não) ")
            if pergunta == '1':
                self.questionario_experiencia_prof()
            elif pergunta == '2':
                break
            else: print("Digite um número válido!")

            continuar = input("Deseja continuar adicionando formações? (1 - Sim / 2 - Não) ")
            if continuar == '1':
                self.questionario_experiencia_prof()
            elif continuar == '2':
                break
            else: print("Digite um número válido!")
    def questionario_experiencia_prof(self):
        while True:
            formacao = input("Digite o nome da formação: ")
            if len(formacao) == 0:
                print("Digite algo!")
            else:
                while True:
                    inicio = input(f"Digite a data de começo na formação {formacao.title()} (MM/AAAA): ")
                    if self.__tratador.tratar_mes_ano(inicio):
                        while True:
                            fim = input(f"Digite a data de término da formação {formacao.title()} (MM/AAAA):")
                            if self.__tratador.tratar_mes_ano(fim):
                                self.__armazenar.armazenar_dado({"Formação": formacao, "Início": inicio, "Término": fim})
                                return
                            else:
                                pass
                    else:
                        pass


