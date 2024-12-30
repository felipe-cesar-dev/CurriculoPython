from Model.ClassesConcretas.ArmazenarDados import ArmazenarDados
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.NomeView import Nome

t = TratarPalavraConcreta()
b = ArmazenarDados()
a = Nome(t,b)
a.capturar_dados()

print(b.get_nome())
