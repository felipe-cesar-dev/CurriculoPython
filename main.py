from Controller.ClassesConcretas.ControleArmazenamentoConcreto import ControleArmazenamentoConcreto
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.BancodeDados import BancodeDados
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.DadosPrincipais import NomeView
from View.ClassesConcretas.InfosPessoais.EstadoCivilView import EstadoCivil

bd = BancodeDados()
bd.conectar()
a = NomeView(ControleTratamento(TratarPalavraConcreta()),ControleArmazenamentoConcreto(BancodeDados()))
b = EstadoCivil(ControleTratamento(TratarPalavraConcreta()), ControleArmazenamentoConcreto(BancodeDados()))
a.capturar_dados()
b.capturar_dados()
bd.fechar_conexao()