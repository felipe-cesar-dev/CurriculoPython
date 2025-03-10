from abc import ABC, abstractmethod


class BuilderAbstract(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def construir_sessao(self):
        pass
