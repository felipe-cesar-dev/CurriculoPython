from Model.ClassesConcretas.ArmazenarRedesSociais import ArmazenarRedesSociais
from Model.Tratadores.TratarRedeConcreta import TratarRedeConcreta
from View.ClassesConcretas.RedesSociais.RedesView import Rede

ar = ArmazenarRedesSociais()
t=TratarRedeConcreta()
a=Rede(t, ar)

a.capturar_dados()

print(ar.get_dado())