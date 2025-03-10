from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.ArmazenarDadosPrincipais import ArmazenarDadosPrincipais
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.DadosPrincipais import NomeView


class BuilderDadosPrincipais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__dadosPrincipais = ''


    def construir_sessao(self):
        controleArmazenamento = ControleArmazenamento(ArmazenarDadosPrincipais())
        self.__dadosPrincipais = NomeView(ControleTratamento(TratarPalavraConcreta()), controleArmazenamento)
        self.__dadosPrincipais.capturar_dados()
