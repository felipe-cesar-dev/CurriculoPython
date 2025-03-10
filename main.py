from Controller.ClassesAbstratas.ControleArmazenamentoAbs import ControleArmazenamentoAbs
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesAbstratas.Armazenar import Armazenar
from Model.ClassesConcretas.ArmazenarDadosPrincipais import ArmazenarDadosPrincipais
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.NomeView import NomeView
from View.ClassesConcretas.DadosPrincipais.ProfissaoView import Profissao

a = ControleArmazenamento(ArmazenarDadosPrincipais())
b = ControleTratamento(TratarPalavraConcreta())
c = NomeView(b,a)

c.capturar_dados()



