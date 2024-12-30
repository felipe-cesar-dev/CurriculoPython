from View.ClassesConcretas.DadosPrincipais.NomeView import Nome

class GetDados:
    def __init__(self, nome = Nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome