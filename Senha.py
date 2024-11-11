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


class Convenio(Base):
   

    def __repr__(self):
        return f'<Convenio(empresa={self.empresa}, numero={self.numero}, plano={self.plano})>'

    def __init__(self, empresa, numero, plano):
        self.empresa = empresa
        self.numero = numero
        self.plano = plano

