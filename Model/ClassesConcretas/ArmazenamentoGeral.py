class ArmazenamentoGeral:
    def __init__(self):
        self.dadosGerais = []

    def armazenar_dados_gerais(self, dado):
        self.dadosGerais.append(dado)

    def get_dados_gerais(self):
        return self.dadosGerais