from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Definição do Base, necessário para criar as tabelas
Base = declarative_base()

class Convenio(Base):
    __tablename__ = 'convenios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa = Column(String)
    numero = Column(Integer, unique=True)
    plano = Column(String)

    def __repr__(self):
        return f'<Convenio(empresa={self.empresa}, numero={self.numero}, plano={self.plano})>'

    def __init__(self, empresa, numero, plano):
        self.empresa = empresa
        self.numero = numero
        self.plano = plano


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String, unique=True)  # Usando String para CPF
    rg = Column(String, unique=True)   # Usando String para RG
    idade = Column(Integer)
    convenio_id = Column(Integer, ForeignKey('convenios.id'))  # Relacionamento com 'convenios'
    convenio = relationship('Convenio', backref='pacientes')

    def __repr__(self):
        return f'<Paciente(nome={self.nome}, cpf={self.cpf}, convenio={self.convenio.numero})>'

    def __init__(self, nome, cpf, rg, idade, convenio=None):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.convenio = convenio