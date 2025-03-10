from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Controller.ClassesConcretas.ControleTratamentoDataNasc import ControleTratamentoDataNasc
from Model.ClassesConcretas.ArmazenarInfosPessoais import ArmazenarInfosPessoais
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.InfosPessoais.DataNascimentoView import DataNascimento
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil
from View.ClassesConcretas.InfosPessoais.NacionalidadeView import Nacionalidade


class BuilderInfosPessoais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__dataNasc = ''
        self.__estadoC = ''
        self.__nacionalidade = ''

    def construir_sessao(self):
        controleArmazenamento = ControleArmazenamento(ArmazenarInfosPessoais())
        self.__dataNasc = DataNascimento(ControleTratamentoDataNasc(TratarDataConcreta()),controleArmazenamento)
        self.__estadoC = EstadoCivil(ControleTratamento(TratarPalavraConcreta()), controleArmazenamento)
        self.__nacionalidade = Nacionalidade(ControleTratamento(TratarPalavraConcreta()), controleArmazenamento)
        self.__dataNasc.capturar_dados()
        self.__estadoC.capturar_dados()
        self.__nacionalidade.capturar_dados()
