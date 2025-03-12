from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleTratamentoCel import ControleTratamentoCel
from Controller.ClassesConcretas.ControleTratamentoEmail import ControleTratamentoEmail
from Controller.ClassesConcretas.ControleTratamentoEndereco import ControleTratamentoEndereco
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from Model.Tratadores.TratarEmailConcreto import TratarEmailConcreto
from Model.Tratadores.TratarEnderecoConcreto import TratarEnderecoConcreto
from View.ClassesConcretas.InfosContato.CelularView import Celular
from View.ClassesConcretas.InfosContato.EmailView import Email
from View.ClassesConcretas.InfosContato.EnderecoView import Endereco


class BuilderInfosContato(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__dados = []
        self.__celular = ''
        self.__email = ''
        self.__endereco = ''

    def construir_sessao(self):
        celular = Celular(ControleTratamentoCel(TratarCelularConcreto()))
        email = Email(ControleTratamentoEmail(TratarEmailConcreto()))
        endereco = Endereco(ControleTratamentoEndereco(TratarEnderecoConcreto()))
        celular.capturar_dados()
        email.capturar_dados()
        endereco.capturar_dados()
        self.__celular = (celular.get_dado())
        self.__email = (email.get_dado())
        self.__endereco = (endereco.get_dado())
        return self.__dados.append([self.__celular, self.__email, self.__endereco])

    def get_dados(self):
        return self.__dados