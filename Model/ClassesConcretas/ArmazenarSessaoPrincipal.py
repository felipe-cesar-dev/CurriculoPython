from Model.ClassesAbstratas.Armazenar import Armazenar


class ArmazenarSessaoPrincipal(Armazenar):
 def __init__(self):
    super().__init__()
    self.__dado = []

 def armazenar_dado(self, dado):
    self.__dado.append(dado)

 def get_dado(self):
    return f'Tópicos da sessão Principal: {self.__dado}'