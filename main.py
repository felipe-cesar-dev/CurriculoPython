from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamentoCel import ControleTratamentoCel
from Controller.ClassesConcretas.ControleTratamentoEmail import ControleTratamentoEmail
from Controller.ClassesConcretas.ControleTratamentoEndereco import ControleTratamentoEndereco
from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from Model.Tratadores.TratarEmailConcreto import TratarEmailConcreto
from Model.Tratadores.TratarEnderecoConcreto import TratarEnderecoConcreto
from View.ClassesConcretas.InfosContato.CelularView import Celular
from View.ClassesConcretas.InfosContato.EmailView import Email
from View.ClassesConcretas.InfosContato.EnderecoView import Endereco

armaz = ArmazenarInfosContato()
cArmaz = ControleArmazenamento(armaz)

tratar = TratarCelularConcreto()
cTratar = ControleTratamentoCel(tratar)

etratar = TratarEnderecoConcreto()
Etratar = ControleTratamentoEndereco(etratar)



a = Celular(cTratar, cArmaz)
a.capturar_dados()

btratou = TratarEmailConcreto()
bTratar = ControleTratamentoEmail(btratou)

b = Email(bTratar, cArmaz)

b.capturar_dados()

c = Endereco(Etratar, cArmaz)
c.capturar_dados()