from Controller.ClassesConcretas.ControleArmazenamentoConcreto import ControleArmazenamentoConcreto
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.ArmazenamentoGeral import ArmazenamentoGeral
from Model.ClassesConcretas.BancodeDados import BancodeDados
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.Nome import NomeView
from View.ClassesConcretas.DadosPrincipais.Profissao import Profissao
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil


db = BancodeDados()
db.fechar_conexao()
db.conectar()
geral = ArmazenamentoGeral()
a = NomeView(ControleTratamento(TratarPalavraConcreta()),ControleArmazenamentoConcreto(BancodeDados()))
b = EstadoCivil(ControleTratamento(TratarPalavraConcreta()), ControleArmazenamentoConcreto(BancodeDados()))
c = Profissao(ControleTratamento(TratarPalavraConcreta()), ControleArmazenamentoConcreto(BancodeDados()))
a.capturar_dados()
geral.armazenar_dados_gerais(a.get_dados())
b.capturar_dados()
geral.armazenar_dados_gerais(b.get_dados())
c.capturar_dados()
geral.armazenar_dados_gerais(c.get_dados())

print(geral.get_dados_gerais())


