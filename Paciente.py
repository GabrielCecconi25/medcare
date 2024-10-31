class Paciente:
    def __init__(self, nome, cpf, rg, idade, convenio=None):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.convenio = convenio
    
    def geNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def getRg(self):
        return self.rg
    
    def setRg(self, rg):
        self.rg = rg
    
    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getConvenio(self):
        return self.convenio
    
    def setConvenio(self, convenio):
        self.convenio = convenio

 class Convenio:
     def __init__(self, empresa, numero, plano):
        self._empresa = empresa
        self._numero = numero
        self._plano = plano

    def get_Empresa(self):
        return self._empresa
    
    def set_Empresa(self, empresa):
        self._empresa = empresa

    def get_Numero(self):
        return self._numero
    
    def set_Numero(self, numero):
        self._numero = numero
    
    def get_Plano(self):
        return self._plano
    
    def set_Plano(self, plano):
        self._plano = plano
