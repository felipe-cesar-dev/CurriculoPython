
class ArmazenamentoGeral:
    def __init__(self):
        super().__init__()
        self.__armazenamento = []

    def armazenenamento(self, dado):
        self.__armazenamento.append(dado)

    def imprimir_armazenamento(self):
        print(f'Itens armazenados: {self.__armazenamento}')