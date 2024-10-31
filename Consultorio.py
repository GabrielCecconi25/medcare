class Consultorio:
    def __init__(self, numero, status=Livre):
        self.numero = numero
        self.__status = status

    def ocuparSala(self, medico, senha):
        self.__status = ocupada
        gerenciarSala(self.numero, medico, senha)
    
    def desocuparSala(self)
        self.__status = desocupada
    

