from Model.ClassesAbstratas.BancodeDadosAbs import BancodeDadosAbs
import sqlite3

class BancodeDados(BancodeDadosAbs):
    def __init__(self):
        super().__init__()
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect('db.db')
        self.cursor = self.conexao.cursor()

        # Criar tabela principal
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_unicos (
                nome TEXT PRIMARY KEY,
                profissao TEXT,
                celular TEXT,
                email TEXT,
                endereco TEXT,
                data_de_nascimento TEXT,
                estado_civil TEXT,
                nacionalidade TEXT,
                sobre_mim TEXT
            );
        ''')

        # Criar tabela experiência profissional
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS experiencia_profissional (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
            );
        ''')

        # Criar tabela formação acadêmica
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS formacao_academica (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
            );
        ''')

        # Criar tabela conhecimentos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conhecimentos_cursos (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
            );
        ''')

        # Criar tabela redes sociais
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS redes_sociais (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                link TEXT,
                FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
            );
        ''')

        # Criar tabela sobre mim
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sobre_mim (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
            );
        ''')

        self.conexao.commit()

    def armazenar_primary_key(self, nome, tabela, coluna):
        if not self.conexao:
            self.conectar()
        self.cursor.execute(f"INSERT INTO {tabela} (nome) VALUES (?)", (nome,))
        self.conexao.commit()

    def update_linha(self, nome, tabela, coluna, dado):
        if not self.conexao:
            self.conectar()
        self.cursor.execute(f"UPDATE {tabela} SET {coluna} = ? WHERE nome = ?", (dado, nome))
        self.conexao.commit()

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()


#banco_de_dados = BancodeDados()

# Inserir um novo registro na tabela "dados_unicos"
#banco_de_dados.armazenar_primary_key("Rebeca", "dados_unicos", "nome")

# Atualizar o registro da tabela "dados_unicos" onde o nome é "João"
#banco_de_dados.update_linha("Rebeca", "dados_unicos", "celular", "(32)99177-5555")

# Fechar a conexão com o banco de dados
#banco_de_dados.fechar_conexao()

