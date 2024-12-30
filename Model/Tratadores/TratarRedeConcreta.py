from Model.ClassesAbstratas.TratarRede import TratarRede


class TratarRedeConcreta(TratarRede):
    def tratar_rede(self, link: str, pergunta=''):
        while True:
            pergunta = input(f"Gostaria de adicionar sua conta no {link.title()}? (s/n) ")
            if pergunta.strip().lower() == 's':
                while True:
                    rede = input(f'Digite o link do seu {link.title()} (ex: {link}.com/blablabla): ')
                    if len(rede) == 0 or rede.isdigit():
                        print('Digite um link válido')
                    else:
                        return rede
            elif pergunta.strip().lower() == 'n':
                break
            else:
                print("Digite uma resposta válida (s/n)!")

    def remover_Nones(self, array):
        for d in array[:]:
            if None in d.values():
                array.remove(d)