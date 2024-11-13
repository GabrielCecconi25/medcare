from Banco import criar_banco, get_session
import Atendimento
from CadastroPaciente import CadastroSenha

from Convenio import Convenio
from Paciente import Paciente
from Senha import Senha
from Medico import Medico
from Consultorio import Consultorio


def main():
    # Cria banco de dados SQLite
    criar_banco()

    # cod = int(input("Quem está operando o sistema, "))
    cod = int(input("1. Paciente\n2. Cadastrar Senha\n3. Medico\n4. Fila\n5. Sala\nEscolher opção inicial: "))
    if cod == 1:
        pac = int(input("1. Cadastrar Paciente\n2. Alterar Dados de Pacinete\n3. Pegar Dados do Paciente\n"))
    elif cod == 2:
        sen = CadastroSenha()
        sen.main()

main()
