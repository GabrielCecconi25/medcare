class Senha:
    def __init__(self, paciente):
        self.paciente = paciente
        setNumero()
    
    def setNumero(self):
        # Logica para gerar uma senha
        # que não esteja registrada no banco
        self.numero = numero