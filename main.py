from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamentoCel import ControleTratamentoCel
from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarCelularConcreto import TratarCelularConcreto
from View.ClassesConcretas.InfosContato.CelularView import Celular

armaz = ArmazenarInfosContato()
cArmaz = ControleArmazenamento(armaz)

tratar = TratarCelularConcreto()
cTratar = ControleTratamentoCel(tratar)

a = Celular(cTratar, cArmaz)
a.capturar_dados()