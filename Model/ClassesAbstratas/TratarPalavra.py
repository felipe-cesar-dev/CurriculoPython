from abc import ABC, abstractmethod

class TratarpalavraAbstrata(ABC):
    @abstractmethod
    def verificar_len_zero(self, palavra):
        pass

    @abstractmethod
    def verificar_tem_numero(self, palavra):
        pass

    @abstractmethod
    def tratar_palavra(self, palavra):
        self.verificar_len_zero(palavra)
        self.verificar_tem_numero(palavra)