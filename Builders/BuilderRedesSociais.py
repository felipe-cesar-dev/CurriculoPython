from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Model.ClassesConcretas.ArmazenarRedesSociais import ArmazenarRedesSociais
from View.ClassesConcretas.RedesSociais.RedesView import RedeView


class BuilderRedesSociais(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__redesSociais = ''


    def construir_sessao(self):
        controleArmazenamento = ControleArmazenamento(ArmazenarRedesSociais())
        self.__redesSociais = RedeView(controleArmazenamento)
        self.__redesSociais.capturar_dados()

