from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from Banco import Base

class Convenio(Base):
    __tablename__ = 'convenio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa = Column(String)
    numero = Column(Integer, unique=True)
    plano = Column(String)

    paciente = relationship("Paciente", back_populates="convenio")

    def __repr__(self):
        return f'<Convenio(empresa={self.empresa}, numero={self.numero}, plano={self.plano})>'

    def __init__(self, empresa, numero, plano):
        self.empresa = empresa
        self.numero = numero
        self.plano = plano