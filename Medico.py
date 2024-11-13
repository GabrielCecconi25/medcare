from sqlalchemy import Column, Integer, String

from Banco import Base

class Medico(Base):
    __tablename__ = 'medico'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    crm = Column(Integer, unique=True)
    especialidade = Column(String)

    def __repr__(self):
        return f'<Medico(nome={self.nome}, crm={self.crm}, especialidade={self.especialidade})>'

    def __init__(self, crm, nome, especialidade):
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade
