from abc import ABC, abstractmethod


class Armazenar(ABC):
    def __init__(self):
        self.__dado = []

    @abstractmethod
    def armazenar_dado(self, dado):
        pass
    @abstractmethod
    def get_dado(self):
        pass