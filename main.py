import Atendimento, CadastroPaciente
from CadastroPaciente import CadastroSenha

def main():
    #cod = int(input("Quem está operando o sistema, "))
    cod = int(input("1. Paciente\n2. Cadastrar Senha\n3. Medico\n4. Fila\n5. Sala\nEscolher opção inicial: "))
    if cod == 1:
        pac = int(input("1. Cadastrar Paciente\n2. Alterar Dados de Pacinete\n3. Pegar Dados do Paciente\n"))
    elif cod == 2:
        sen = CadastroSenha()
        sen.main()

main()