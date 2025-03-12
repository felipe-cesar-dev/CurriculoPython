from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.BancodeDados import BancodeDados
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.DadosPrincipais.Nome import NomeView
from View.ClassesConcretas.DadosPrincipais.Profissao import Profissao

a = NomeView(ControleTratamento(TratarPalavraConcreta()))
b = Profissao(ControleTratamento(TratarPalavraConcreta()))
a.capturar_dados()
b.capturar_dados()

nome = str(a.get_dados()).replace("['", '').replace("']", '')
profissao = str(b.get_dados()).replace("['", '').replace("']", '')

bd = BancodeDados()
bd.armazenar_dado(nome, 'dados_unicos', 'profissao', profissao)
bd.fechar_conexao()






