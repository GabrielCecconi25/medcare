from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Banco import Base, get_session
from Paciente import Paciente

class Senha(Base):
    __tablename__ = 'senha'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
    numero = Column(Integer)
    horario = Column(String)
    paciente_id = Column(Integer, ForeignKey('paciente.id'))

    paciente = relationship("Paciente", back_populates="senhas")

    
    def __init__(self, paciente, session):
        self.paciente = paciente
        self.status = "em espera"
        self.setNumero(session)

    def setNumero(self, session):
        session.flush()

        # Recuperar o último número de senha gerado
        ultima_senha = session.query(Senha).order_by(Senha.numero.desc()).first()

        if ultima_senha:
            self.numero = ultima_senha.numero + 1 # Incrementa o número da última senha
        else:
            self.numero = 1  # Primeira senha a ser gerada

        # Define o horário atual da criação da senha
        self.horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
