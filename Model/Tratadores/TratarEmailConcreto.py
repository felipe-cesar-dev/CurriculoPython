from Model.ClassesAbstratas.TratarEmail import TratarEmail
import re


class TratarEmailConcreto(TratarEmail):
    def tratar_email(self, email):
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
            raise ValueError('Digite um email válido (exemplo@exemplo.exemplo)!')
        else:
            return email

