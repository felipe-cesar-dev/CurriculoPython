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

    def tratar_mes_ano(self, mesAno):
        dataminima = datetime.strptime('01/1900', '%m/%Y')
        datamax = datetime.now()

        try:
            data = datetime.strptime(mesAno, '%m/%Y')
            if data < dataminima or data > datamax:
                raise ValueError("Digite uma data entre 01/1900 e a data atual")
            return mesAno
        except ValueError as e:
            if "unconverted data remains" in str(e) or "time data" in str(e):
                print("Data inválida")
            else:
                print(f"Erro: {e}")
            return None





