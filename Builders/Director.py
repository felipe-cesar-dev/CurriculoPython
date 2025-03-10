from Builders.BuilderDadosPrincipais import BuilderDadosPrincipais
from Builders.BuilderInfosContato import BuilderInfosContato
from Builders.BuilderInfosPessoais import BuilderInfosPessoais
from Builders.BuilderRedesSociais import BuilderRedesSociais
from Builders.BuilderSessaoPrincipal import BuilderSessaoPrincipal

class Director:
    dadosPrincipais = BuilderDadosPrincipais()
    infosContato = BuilderInfosContato()
    infosPessoais = BuilderInfosPessoais()
    redesSociais = BuilderRedesSociais()
    sessaoPrincipal = BuilderSessaoPrincipal()

    dadosPrincipais.construir_sessao()
    infosContato.construir_sessao()
    infosPessoais.construir_sessao()
    redesSociais.construir_sessao()
    sessaoPrincipal.construir_sessao()