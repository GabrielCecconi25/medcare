from sqlalchemy import Column, Integer, String

from Banco import Base

class Consultorio(Base):
    __tablename__ = 'consultorio'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer)
    status = Column(String)

    def __init__(self, numero, status="Desocupada"):
        self.numero = numero
        self.__status = status

    def ocuparSala(self, medico, senha):
        self.__status = "Ocupada"
        # gerenciarSala(self.numero, medico, senha)
    
    def desocuparSala(self):
        self.__status = "Desocupada"
    

