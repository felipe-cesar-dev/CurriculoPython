from Builders.BuilderAbstract import BuilderAbstract
from View.ClassesConcretas.RedesSociais.RedesView import RedeView


class BuilderRedesSociais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__redesS = ''
        self.__dados = []

    def construir_sessao(self):
        rede = RedeView()
        rede.capturar_dados()
        self.__redesS = rede.get_dado()
        return self.__dados.append(self.__redesS)


    def get_dados(self):
        return self.__dados
