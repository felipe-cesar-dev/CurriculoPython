from Model.ClassesAbstratas.ArmazenamentoGeralAbs import ArmazenamentoGeralAbs


class ArmazenamentoGeral(ArmazenamentoGeralAbs):
    def __init__(self):
        super().__init__()
        self.dadosGerais = []

    def armazenar_dados_gerais(self, dado):
        self.dadosGerais.append(dado)

    def get_dados_gerais(self):
        return self.dadosGerais