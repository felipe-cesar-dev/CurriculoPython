from Controller.ClassesConcretas.ControleArmazenamentoConcreto import ControleArmazenamentoConcreto
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.BancodeDados import BancodeDados
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.Nome import NomeView
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil

dados = []

a = NomeView(ControleTratamento(TratarPalavraConcreta()),ControleArmazenamentoConcreto(BancodeDados()))
b = EstadoCivil(ControleTratamento(TratarPalavraConcreta()), ControleArmazenamentoConcreto(BancodeDados()))
a.capturar_dados()
dados.append(a.get_dados())
b.capturar_dados()
dados.append(b.get_dados())

print(dados)
