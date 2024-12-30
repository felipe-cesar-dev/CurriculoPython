from Model.ClassesAbstratas.TratarData import TratarData
from datetime import datetime


class TratarDataConcreta(TratarData):
    def tratar_data(self, data):
        if datetime.strptime(data, '%d/%m/%Y'):
            return data

    def tratar_ano(self, ano = None):
        while True:
            try:
                ano = int(input("Digite o ano que você começou na empresa: "))
                min_ano = 1500
                max_ano = datetime.now().year
                if min_ano <= ano <= max_ano:
                    return ano
                else:
                    raise ValueError(f'Digite um ano entre {min_ano} e {max_ano}')
            except ValueError as e:
                print(e)



