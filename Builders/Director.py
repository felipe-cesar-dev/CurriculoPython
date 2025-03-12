from Builders.BuilderDadosPrincipais import BuilderDadosPrincipais
from Builders.BuilderInfosContato import BuilderInfosContato
from Builders.BuilderInfosPessoais import BuilderInfosPessoais
from Builders.BuilderRedesSociais import BuilderRedesSociais
from Builders.BuilderSessaoPrincipal import BuilderSessaoPrincipal

class Director:
    def __init__(self):
        pass

    def aplicacao(self):
        dados_principais = BuilderDadosPrincipais()
        dados_principais.construir_sessao()

        infos_contato = BuilderInfosContato()
        infos_contato.construir_sessao()

        infos_pessoais = BuilderInfosPessoais()
        infos_pessoais.construir_sessao()

        redes_sociais = BuilderRedesSociais()
        redes_sociais.construir_sessao()

        sessao_principal = BuilderSessaoPrincipal()
        sessao_principal.construir_sessao()