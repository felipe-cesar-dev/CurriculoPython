import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('../../Model/ClassesConcretas/curriculo.db')

# Criar um cursor
cursor = conexao.cursor()

# Criar tabela principal
cursor.execute('''
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
cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiencia_profissional (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        data_inicio TEXT,
        data_fim TEXT,
        FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
    );
''')

# Criar tabela formação acadêmica
cursor.execute('''
    CREATE TABLE IF NOT EXISTS formacao_academica (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        data_inicio TEXT,
        data_fim TEXT,
        FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
    );
''')

# Criar tabela conhecimentos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS conhecimentos_cursos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
    );
''')

# Criar tabela redes sociais
cursor.execute('''
    CREATE TABLE IF NOT EXISTS redes_sociais (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        link TEXT,
        FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sobre_mim (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        FOREIGN KEY (nome) REFERENCES dados_unicos (nome)
    );
''')

# Commitar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()