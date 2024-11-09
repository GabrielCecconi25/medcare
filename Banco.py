import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Paciente import Base  # Importando Base do Paciente.py, onde as classes de modelo estão definidas

# Função para criar o banco de dados
def criar_banco():
    # Verificar se a pasta "banco" existe. Se não, criar.
    pasta_banco = 'banco'
    if not os.path.exists(pasta_banco):
        os.makedirs(pasta_banco)  # Cria a pasta 'banco' se não existir
        print(f"Pasta '{pasta_banco}' criada com sucesso!")

    # Caminho para o arquivo do banco de dados dentro da pasta 'banco'
    caminho_banco = os.path.join(pasta_banco, 'medcare.db')

    # Cria a conexão com o banco SQLite
    engine = create_engine(f'sqlite:///{caminho_banco}', echo=True)

    # Cria as tabelas definidas no Base (a partir dos modelos em Paciente.py)
    Base.metadata.create_all(engine)

    print(f"Banco de dados '{caminho_banco}' criado com sucesso!")

    # Retorna a engine e session para uso externo
    Session = sessionmaker(bind=engine)
    session = Session()

    return engine, session

# Chama a função para criar o banco (criar as tabelas) e retorna a engine e session
if __name__ == "__main__":
    criar_banco()