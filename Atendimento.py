from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Banco import Base
from Consultorio import Consultorio
from Medico import Medico
from Paciente import Paciente

class Atendimento(Base):
    __tablename__ = 'atendimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
    horario_inicio = Column(String)
    horario_termino = Column(String)
    paciente_id = Column(Integer, ForeignKey('paciente.id'))
    medico_id = Column(Integer, ForeignKey('medico.id'))
    consultorio_id = Column(Integer, ForeignKey('consultorio.id'))

    paciente = relationship("Paciente", back_populates="atendimento")
    medico = relationship("Medico", back_populates="atendimento")
    consultorio = relationship("Consultorio", back_populates="atendimento")


    def __init__(self, paciente, medico, consultorio):
        self.status = "em andamento"
        self.paciente = paciente
        self.medico = medico
        self.consultorio = consultorio

    def encerrarAtendimento(self):
        self.status = "encerrado"
