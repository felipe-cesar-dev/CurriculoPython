from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleTratamentoCel import ControleTratamentoCel
from Controller.ClassesConcretas.ControleTratamentoEmail import ControleTratamentoEmail
from Controller.ClassesConcretas.ControleTratamentoEndereco import ControleTratamentoEndereco
from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from Model.Tratadores.TratarEmailConcreto import TratarEmailConcreto
from Model.Tratadores.TratarEnderecoConcreto import TratarEnderecoConcreto
from View.ClassesConcretas.InfosContato.EnderecoView import Endereco
from View.ClassesConcretas.InfosContato.EmailView import Email
from View.ClassesConcretas.InfosContato.CelularView import Celular
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento


class BuilderInfosContato(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__celular = int
        self.__email = ''
        self.__endereco = ''

    def construir_sessao(self):
        controleArmazenamento = ControleArmazenamento(ArmazenarInfosContato())
        self.__celular = Celular(ControleTratamentoCel(TratarCelularConcreto()), controleArmazenamento)
        self.__endereco = Endereco(ControleTratamentoEndereco(TratarEnderecoConcreto()), controleArmazenamento)
        self.__email = Email(ControleTratamentoEmail(TratarEmailConcreto()), controleArmazenamento)
        self.__celular.capturar_dados()
        self.__endereco.capturar_dados()
        self.__email.capturar_dados()
