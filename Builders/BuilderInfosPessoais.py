from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Controller.ClassesConcretas.ControleTratamentoDataNasc import ControleTratamentoDataNasc
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.InfosPessoais.DataNascimentoView import DataNascimento
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil
from View.ClassesConcretas.InfosPessoais.NacionalidadeView import Nacionalidade


class BuilderInfosPessoais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__dados = []
        self.__dataNasc = ''
        self.__estadoc = ''
        self.__nacinalidade = ''

    def construir_sessao(self):
        dataNasc = DataNascimento(ControleTratamentoDataNasc(TratarDataConcreta()))
        estadoC = EstadoCivil(ControleTratamento(TratarPalavraConcreta()))
        nacionalidade = Nacionalidade(ControleTratamento(TratarPalavraConcreta()))
        dataNasc.capturar_dados()
        estadoC.capturar_dados()
        nacionalidade.capturar_dados()
        self.__estadoc = estadoC.get_dados()
        self.__dataNasc = dataNasc.get_dado()
        self.__nacinalidade = nacionalidade.get_dado()
        return self.__dados.append([self.__dataNasc, self.__estadoc, self.__nacinalidade])

    def get_dados(self):
        return self.__dados