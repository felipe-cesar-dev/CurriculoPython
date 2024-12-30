
class ArmazenarDados:
 def __init__(self):
    self.__nome = ""

 def armazenar_nome(self, nome):
    self.__nome = nome

 def get_nome(self):
    return self.__nome