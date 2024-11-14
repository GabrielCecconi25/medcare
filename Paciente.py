from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Banco import Base
from Convenio import Convenio

class Paciente(Base):
    __tablename__ = 'paciente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(Integer, unique=True)
    rg = Column(Integer)
    idade = Column(Integer)
    convenio_id = Column(Integer, ForeignKey('convenio.id'))

    convenio = relationship("Convenio", back_populates="paciente")
    
    senha = relationship("Senha", back_populates="paciente")
    atendimento = relationship("Atendimento", back_populates="paciente")

    def __repr__(self):
        return f'<Paciente(nome={self.nome}, cpf={self.cpf}, convenio={self.convenio.numero})>'

    def __init__(self, nome, cpf, rg, idade, convenio=None):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.convenio = convenio

    def deletar_paciente(self, id_paciente, session=None):
        # Deleta um paciente pelo ID.
        paciente = session.query(Paciente).filter_by(id=id_paciente).first()
        if paciente:
            session.delete(paciente)
            session.commit()
            print(f"Paciente com ID {id_paciente} foi deletado.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado.")

    def listar_pacientes(self, session=None):
        # Lista todos os pacientes na tabela.
        pacientes = session.query(Paciente).all()
        for paciente in pacientes:
            print(paciente)