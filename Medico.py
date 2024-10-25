
class Medico :
    def __init__(self, crm, nome, especialidade):
        self.__crm = crm
        self.__nome = nome
        self.__especialidade = especialidade
    
    def get_crm(self):
        return self.__crm

    def set_crm(self, crm):
        self.__crm = crm
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade