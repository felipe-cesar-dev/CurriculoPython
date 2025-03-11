import sqlite3

class BancoDeDados:
    def __init__(self, nome_do_banco):
        self.nome_do_banco = nome_do_banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_do_banco)
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

    def criar_tabela(self, nome_da_tabela, colunas):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {nome_da_tabela} (
                {', '.join([f'{coluna} TEXT' for coluna in colunas])}
            );
        ''')
        self.conexao.commit()

    def inserir_dados(self, nome_da_tabela, dados):
        self.cursor.execute(f'''
            INSERT INTO {nome_da_tabela} VALUES (
                {', '.join(['?'] * len(dados))}
            );
        ''', dados)
        self.conexao.commit()

    def selecionar_dados(self, nome_da_tabela):
        self.cursor.execute(f'''
            SELECT * FROM {nome_da_tabela};
        ''')
        return self.cursor.fetchall()
