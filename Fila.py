from Banco import get_session
from Paciente import Paciente
from Senha import Senha

class Fila():
    def __init__(self):
        self.__senhas = []
        self.__fim = 0

    def vazia(self):
        return self.__fim == 0
    
    def enfileira(self, senha):
        self.__senhas.append(senha)
        self.__fim += 1
    
    def desenfileira(self):
        if self.vazia():
            raise FilaVazia('Fila do Atendimento vazia.')
        senha = self.__senhas[0]
        for i in range(1, self.__fim):
            self.__senhas[i-1] = self.__senhas[i]
        self.__fim -= 1
        return senha

    def getFila(self):
        if self.vazia():
            raise FilaVazia('Fila do Atendimento vazia.')
        for i in self.__senhas:
            print(i)
    
    def criarSenha(self, paciente, session):
        # Cria senha
        senha = Senha(paciente, session)
        session.commit()
        return senha.numero
            


    
        
class FilaVazia(Exception):
    pass