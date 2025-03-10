from Builders.BuilderDadosPrincipais import BuilderDadosPrincipais
from Builders.BuilderRedesSociais import BuilderRedesSociais
from Model.ClassesConcretas.ArmazenamentoGeral import ArmazenamentoGeral

c = ArmazenamentoGeral()

a = BuilderDadosPrincipais()
b = BuilderRedesSociais()

a.construir_sessao()
b.construir_sessao()

c.armazenenamento(a)
c.armazenenamento(b)

c.imprimir_aramanemanto()

