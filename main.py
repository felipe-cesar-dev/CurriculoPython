from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from Model.Tratadores.TratarEmailConcreto import TratarEmailConcreto
from Model.Tratadores.TratarEnderecoConcreto import TratarEnderecoConcreto
from View.ClassesConcretas.InfosContato.CelularView import Celular
from View.ClassesConcretas.InfosContato.EmailView import Email
from View.ClassesConcretas.InfosContato.EnderecoView import Endereco

t = TratarCelularConcreto()
u = TratarEnderecoConcreto()
ar = ArmazenarInfosContato()

a = Celular(t, ar)
a.capturar_dados()

b = Endereco(u, ar)
b.capturar_dados()


print(ar.get_dado())