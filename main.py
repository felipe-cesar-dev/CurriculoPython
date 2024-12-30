from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from View.ClassesConcretas.InfosContato.CelularView import Celular

t = TratarCelularConcreto()
ar = ArmazenarInfosContato()

a = Celular(t, ar)
a.capturar_dados()

print(ar.get_dado())