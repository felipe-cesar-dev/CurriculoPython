from abc import ABC, abstractmethod

class TratarEmail(ABC):
    @abstractmethod
    def tratar_email(self, email):
        pass