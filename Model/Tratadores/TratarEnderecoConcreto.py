from Model.ClassesAbstratas.TratarEndereco import TratarEndereco


class TratarEnderecoConcreto(TratarEndereco):
    def tratar_endereco(self, endereco):
        if len(endereco) == 0 or endereco.isdigit():
            raise ValueError('Endereço inválido')
        return endereco.title()