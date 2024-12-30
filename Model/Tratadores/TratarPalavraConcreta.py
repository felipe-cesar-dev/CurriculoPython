from Model.ClassesAbstratas.TratarPalavra import TratarpalavraAbstrata


class TratarPalavraConcreta(TratarpalavraAbstrata):
    def verificar_len_zero(self, palavra: str):
        if len(palavra) == 0:
            raise ValueError('Digite algo!')
        return palavra

    def verificar_tem_numero(self, palavra: str):
        if any(caractere.isdigit() for caractere in palavra):
            raise ValueError("Palavra não pode conter números!")
        return palavra

    def tratar_palavra(self, palavra:str):
        self.verificar_len_zero(palavra)
        self.verificar_tem_numero(palavra)

