from Builders.BuilderDadosPrincipais import BuilderDadosPrincipais
from Builders.BuilderInfosContato import BuilderInfosContato
from Builders.BuilderInfosPessoais import BuilderInfosPessoais
from Builders.BuilderRedesSociais import BuilderRedesSociais
from Builders.BuilderSessaoPrincipal import BuilderSessaoPrincipal
from Model.ClassesAbstratas.ArmazenamentoGeralAbs import ArmazenamentoGeralAbs


class Director:
    def __init__(self, armazenar: ArmazenamentoGeralAbs):
        self.__armazenar = armazenar

    def aplicacao(self):
        dados_principais = BuilderDadosPrincipais()
        dados_principais.construir_sessao()
        self.__armazenar.armazenar_dados_gerais(f'Dados Principais: {dados_principais.get_dados()}')

        infos_contato = BuilderInfosContato()
        infos_contato.construir_sessao()
        self.__armazenar.armazenar_dados_gerais(f'Informações de Contato: {infos_contato.get_dados()}')

        infos_pessoais = BuilderInfosPessoais()
        infos_pessoais.construir_sessao()
        self.__armazenar.armazenar_dados_gerais(f'Informações Pessoais: {infos_pessoais.get_dados()}')

        redes_sociais = BuilderRedesSociais()
        redes_sociais.construir_sessao()
        self.__armazenar.armazenar_dados_gerais(f'Redes Sociais: {redes_sociais.get_dados()}')

        sessao_principal = BuilderSessaoPrincipal()
        sessao_principal.construir_sessao()
        self.__armazenar.armazenar_dados_gerais(f'Sessão Principal: {sessao_principal.get_dados()}')

    def get_dados(self):
        return self.__armazenar.get_dados_gerais()
