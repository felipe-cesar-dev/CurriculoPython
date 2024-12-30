from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata
from Model.ClassesConcretas.ArmazenarInfosContato import ArmazenarInfosContato
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.InfosPessoais.DataNascimentoView import DataNascimento
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil
from View.ClassesConcretas.InfosPessoais.NacionalidadeView import Nacionalidade

a1 = TratarDataConcreta()
b1 = TratarPalavraConcreta()

ar = ArmazenarInfosContato()

a = DataNascimento(a1, ar)
a.capturar_dados()
b = EstadoCivil(b1, ar)
b.capturar_dados()
c = Nacionalidade(b1, ar)
c.capturar_dados()

print(ar.get_dado())