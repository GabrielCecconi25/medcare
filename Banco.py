import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Definição do Base, necessário para criar as tabelas
Base = declarative_base()

# Função para criar o banco de dados
def criar_banco():
    pasta_banco = 'banco'
    if not os.path.exists(pasta_banco):
        os.makedirs(pasta_banco)
    caminho_banco = os.path.join(pasta_banco, 'medcare.db')

    # Cria a conexão com o banco SQLite
    engine = create_engine(f'sqlite:///{caminho_banco}', echo=False)
    Base.metadata.create_all(engine)

def get_session():
    caminho_banco = os.path.join('banco', 'medcare.db')
    
    # Cria a engine
    engine = create_engine(f'sqlite:///{caminho_banco}', echo=False)
    
    # Cria a sessão
    Session = sessionmaker(bind=engine)
    session = Session()
    
    return engine, session

