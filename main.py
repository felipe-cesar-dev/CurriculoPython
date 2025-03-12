from Model.ClassesConcretas.ArmazenamentoGeral import ArmazenamentoGeral
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta

from View.ClassesConcretas.SessaoPrincipal.ExperienciaProfissionalView import ExperienciaProfissional

a = ExperienciaProfissional(TratarDataConcreta())
a.capturar_dados()

b=ArmazenamentoGeral()
b.armazenar_dados_gerais(a.get_dado())
print(b.get_dados_gerais())