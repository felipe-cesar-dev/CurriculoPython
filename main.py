from Model.ClassesConcretas.ArmazenarSessaoPrincipal import ArmazenarSessaoPrincipal
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from View.ClassesConcretas.SessaoPrincipal.ExperienciaProfissionalView import ExperienciaProfissional

t = TratarDataConcreta()
ar = ArmazenarSessaoPrincipal()
a = ExperienciaProfissional(t, ar)
a.capturar_dados()

print(ar.get_dado())