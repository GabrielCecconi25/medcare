from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Banco import Base

class Consultorio(Base):
    __tablename__ = 'consultorio'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer)
    status = Column(String)

    atendimento = relationship("Atendimento", back_populates="consultorio")

    def __init__(self, numero, status="Desocupada"):
        self.numero = numero
        self.__status = status

    def ocuparSala(self, medico, senha):
        self.__status = "Ocupada"
        # gerenciarSala(self.numero, medico, senha)
    
    def desocuparSala(self):
        self.__status = "Desocupada"

    def add_consultorio(self, numero, status="Desocupada", session=None):
        #Adiciona um novo consultório à tabela.
        novo_consultorio = Consultorio(numero=numero, status=status)
        session.add(novo_consultorio)
        session.commit()
        print(f"Consultório adicionado: {novo_consultorio}")

    def update_consultorio(self, id_consultorio, novo_numero=None, novo_status=None, session=None):
        #Atualiza os dados de um consultório existente.
        consultorio = session.query(Consultorio).filter_by(id=id_consultorio).first()
        if consultorio:
            if novo_numero:
                consultorio.numero = novo_numero
            if novo_status:
                consultorio.status = novo_status
            session.commit()
            print(f"Consultório atualizado: {consultorio}")
        else:
            print(f"Consultório com ID {id_consultorio} não encontrado.")

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

