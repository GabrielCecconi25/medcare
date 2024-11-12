from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base


# Definição do Base, necessário para criar as tabelas
Base = declarative_base()


class Senha(Base):
    __tablename__ = 'senha'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer)
    paciente_id = Column(Integer, ForeignKey('paciente.id'))
    convenio = relationship('Paciente', backref='pacientes')

    def __init__(self, paciente):
        self.paciente = paciente
        setNumero()

    def setNumero(self):
        # Logica para gerar uma senha
        # que não esteja registrada no banco
        self.numero = numero


def criar_senha(self, session):
    # Recuperar o último número de senha gerado
    ultimo_senha = session.execute(
        'SELECT numero FROM senha ORDER BY numero DESC LIMIT 1').fetchone()

    if ultimo_senha:
        # Incrementa o número da última senha
        numero_senha = ultimo_senha.numero[0] + 1
    else:
        numero_senha = 1  # Primeira senha a ser gerada

    # Criar e adicionar a nova senha diretamente na tabela
    session.execute(
        f"INSERT INTO senha (status, numero) VALUES ('em espera', {numero_senha})")
    session.commit()

    return numero_senha
