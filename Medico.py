from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Banco import Base

class Medico(Base):
    __tablename__ = 'medico'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    crm = Column(Integer, unique=True)
    especialidade = Column(String)

    consultorio = relationship("Consultorio", back_populates="medico")
    atendimento = relationship("Atendimento", back_populates="medico")

    def __repr__(self):
        return f'<Medico(nome={self.nome}, crm={self.crm}, especialidade={self.especialidade})>'

    def __init__(self, crm, nome, especialidade):
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade

    def deletar_medico(self, id_medico, session):
        #Deleta um médico pelo ID.
        medico = session.query(Medico).filter_by(id=id_medico).first()
        if medico:
            session.delete(medico)
            session.commit()
            print(f"Médico com ID {id_medico} foi deletado.")
        else:
            print(f"Médico com ID {id_medico} não encontrado.")

    def listar_medicos(self, session):
        #Lista todos os médicos na tabela.
        medicos = session.query(Medico).all()
        for medico in medicos:
            print(medico)
