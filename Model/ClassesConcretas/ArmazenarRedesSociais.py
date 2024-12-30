from Model.ClassesAbstratas.Armazenar import Armazenar


class ArmazenarRedesSociais(Armazenar):
 def __init__(self):
    super().__init__()
    self.__dado = []

 def armazenar_dado(self, dado):
    self.__dado.append(dado)

 def get_dado(self):
    return f'Redes Sociais: {self.__dado}'