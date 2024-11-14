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
        return f'<Consultorio(numero={self.nome}, status={self.status}>'

    def __init__(self, numero, status="Desocupada"):
        self.numero = numero
        self.status = status

    def ocuparSala(self, medico, senha):
        self.status = "Ocupada"
        # gerenciarSala(self.numero, medico, senha)
    
    def desocuparSala(self):
        self.status = "Desocupada"

    def deletar_consultorio(self, id_consultorio, session=None):
        #Deleta um consultório pelo ID.
        consultorio = session.query(Consultorio).filter_by(id=id_consultorio).first()
        if consultorio:
            session.delete(consultorio)
            session.commit()
            print(f"Consultório com ID {id_consultorio} foi deletado.")
        else:
            print(f"Consultório com ID {id_consultorio} não encontrado.")

    def listar_consultorios(self, session=None):
        #Lista todos os consultórios na tabela.
        consultorios = session.query(Consultorio).all()
        for consultorio in consultorios:
            print(consultorio)

