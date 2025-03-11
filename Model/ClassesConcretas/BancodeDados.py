from Model.ClassesAbstratas.BancodeDadosAbs import BancodeDadosAbs
import sqlite3

class BancodeDados(BancodeDadosAbs):
    def __init__(self):
        super().__init__()
        self.conexao = None
        self.cursor = None

    def conectar(self, nome_do_banco):
        self.conexao = sqlite3.connect('curriculo.db')
        self.cursor = self.conexao.cursor()

    def armazenar_dado(self, tabela, coluna, dado):
        self.cursor.execute(f"INSERT INTO {tabela} ({coluna}) VALUES (?)", (dado,))
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()





