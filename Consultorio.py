from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Banco import Base
from Medico import Medico

class Consultorio(Base):
    __tablename__ = 'consultorio'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True)
    status = Column(String)
    medico_id = Column(Integer, ForeignKey('medico.id'))

    medico = relationship("Medico", back_populates="consultorio")
    atendimento = relationship("Atendimento", back_populates="consultorio")

    def __repr__(self):
        return f'<Consultorio(numero={self.numero}, status={self.status}>'

    def __init__(self, numero):
        self.numero = numero
        self.status = "Desocupado"

    def ocuparSala(self):
        self.status = "Ocupada"
    
    def desocuparSala(self):
        self.status = "Desocupada"
