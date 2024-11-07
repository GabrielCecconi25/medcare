from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(Integer)
    rg = Column(Integer)
    idade = Column(Integer)
    convenio_id = Column(Integer, ForeignKey('convenio.id'))
    convenio = relationship('Convenio', backref='paciente')

    def __repr__(self):
        return f'<Paciente(nome={self.nome}, convenio={self.convenio.numero})>'

    def __init__(self, nome, cpf, rg, idade, convenio=None):
        self.nome = nome
        setCpf(cpf)
        setRg(rg)
        self.idade = idade
        setConvenio(convenio)

    def get_cpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def getRg(self):
        return self.__rg
    
    def setRg(self, rg):
        self.__rg = rg
    
    def getConvenio(self):
        return self.__convenio
    
    def setConvenio(self, convenio):
        self.__convenio = convenio

class Convenio:
    def __init__(self, empresa, numero, plano):
        self._empresa = empresa
        self._numero = numero
        self._plano = plano

    def get_Empresa(self):
        return self._empresa
    
    def set_Empresa(self, empresa):
        self._empresa = empresa

    def get_Numero(self):
        return self._numero
    
    def set_Numero(self, numero):
        self._numero = numero
    
    def get_Plano(self):
        return self._plano
    
    def set_Plano(self, plano):
        self._plano = plano
