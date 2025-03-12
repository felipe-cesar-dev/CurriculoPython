from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.Nome import NomeView
from View.ClassesConcretas.DadosPrincipais.Profissao import Profissao


class BuilderDadosPrincipais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__nome = ''
        self.__profissao = ''
        self.__dados = []

    def construir_sessao(self):
        nome = NomeView(ControleTratamento(TratarPalavraConcreta()))
        profissao = Profissao(ControleTratamento(TratarPalavraConcreta()))
        nome.capturar_dados()
        profissao.capturar_dados()
        self.__nome = (nome.get_dados())
        self.__profissao = (profissao.get_dados())
        return self.__dados.append([self.__nome, self.__profissao])

    def get_dados(self):
        return self.__dados
