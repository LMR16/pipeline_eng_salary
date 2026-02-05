import pandas as pd
from sqlalchemy import create_engine, text
import os
from urllib.parse import quote_plus

caminho_senha = "db/password.txt"

with open(caminho_senha, 'r') as file:

    senha_bruta = file.read()
    db_password = quote_plus(senha_bruta)

# ----Conexão com o banco USANDO PSYCOPG2------ #

'''
print("Conectando ao banco...")
try:
    conn = psycopg2.connect(
        host='localhost', 
        user='postgres_pipeline',
        password=db_password, 
        dbname='example', 
        port=5432
    )

    conn.autocommit = False
    cursor = conn.cursor()
    print("Conectado com sucesso!")

except Exception as e:
    print(f"Erro de conexão {e}")
    exit()
'''

# ----Conexão com o banco USANDO SQLALCHEMY------ #

# Formato: postgresql+psycopg2://USUARIO:SENHA@HOST:PORTA/BANCO
url_conexao = f'postgresql+psycopg2://postgres_pipeline:{db_password}@localhost:5432/example'

try:
    engine = create_engine(url_conexao)
    print("Engine do SQLAlchemy criada com sucesso!")

except Exception as e:
    print(f"Erro ao criar engine: {e}")
    exit()

# ----Extração dos dados ---- #

df = pd.read_csv("./archive/salaries.csv")

# print(df.head())

# --- Limpar a tabela antes de inserir --- #
print("Limpando dados antigos da tabela...")

with engine.connect() as conn:
    # TRUNCATE é muito mais rápido que DELETE e zera tudo instantaneamente.
    # RESTART IDENTITY faz o ID voltar para 1.
    conn.execute(text("TRUNCATE TABLE salarios_engenharia RESTART IDENTITY;"))
    conn.commit()

# ---- Enviando dados para o db ----#

try:
    df.to_sql(
        name='salarios_engenharia', # Nome da tabela
        con=engine,
        if_exists='append',         # 'append' = Adiciona aos dados existentes (não apaga a tabela!)
        index=False,                # False = Não cria uma coluna extra para o índice (0, 1, 2...), pois o postgres ja faz isso
        method='multi',             # Otimização para inserir várias linhas de uma vez
        chunksize=1000              # Envia em pacotes de 1000 para não bloquear a memória
    )
    print("Dados carregados no banco com sucesso!")

except Exception as e:
    print("Falha na carga de dados.")
    print(f"Erro detalhado: {e}")
