from Model.ClassesAbstratas.TratarCelular import TratarCelular
class TratarCelularConcreto(TratarCelular):
    def tratar_celular(self, numero):
        cumprimento = len(str(numero))
        limite = 11
        if not numero.isnumeric() or cumprimento != limite:
            raise ValueError('Número inválido')
        return numero