import re

dados = ["Dados Principais: [[['sadasdasdaswwas'], ['asdasdasdas']]]", "Informações de Contato: [[['99999999999'], ['asdasdsad@asdasd.com'], ['sadawsmsx  asdasdsadasd']]]", "Informações Pessoais: [[['28/08/2000'], ['dedededed'], ['mncmncmxznczx']]]", "Redes Sociais: [[['sdasdasdasd', 'swswswswsws'], ['asdawsas', 'asasxsaxsaxsxa']]]", "Sessão Principal: [[[['asdawsawsa', '02/2000', '04/2024'], ['asdwsawswa', '01/2023', '04/2023']], ['aswwsawswaswsawssdasdasdasd', 'sadawswasadsadasdas'], [['asdasdsadasdasd', '04/2020', '05/2022'], ['asdwsawsaw', '03/2024', '03/2025'], ['asdawswwdscccc', '02/2022', '04/2024']], ['asdasa askxna xasnx aosx sjx  d lsjndc sdlck sdjc sdcsdcs']]]"]

for dado in dados:
    if "Informações de Contato:" in dado:
        # Extrair os índices usando expressão regular
        indices = re.findall(r'\[([^\]]+)\]', dado)
        print(indices)