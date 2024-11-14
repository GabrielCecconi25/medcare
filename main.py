from Banco import criar_banco, get_session
import Atendimento
from CadastroPaciente import CadastroSenha
from Convenio import Convenio
from Paciente import Paciente
from Senha import Senha
from Medico import Medico
from Consultorio import Consultorio
from Fila import Fila


def main():
    # Cria banco de dados SQLite
    criar_banco()

    fila = Fila()

    while True:
        print("Menu:")
        print("1. Paciente")
        print("2. Médico")
        print("3. Fila de Atendimento")
        print("4. Consultório")
        print("0. Sair")
        cod = int(input("Escolher opção inicial: "))
        if cod == 1: # Operações com Paciente
            pac = int(input("1. Cadastrar Paciente\n2. Alterar Dados de Paciente\n3. Pegar Dados do Paciente\n4. Deletar Paciente\n"))
            engine, session = get_session()

            if pac == 1:
                cpf = int(input("Informe o CPF do paciente: "))
                paciente_existente = session.query(Paciente).filter_by(cpf=cpf).first()
                
                if paciente_existente:
                    print("Paciente já cadastrado.")
                else:
                    nome = input("Informe o nome do paciente: ")
                    rg = input("Informe o RG do paciente: ")
                    idade = int(input("Informe a idade do paciente: "))
                    empresa = input("Informe a empresa do convênio: ")
                    numero = int(input("Informe o número do convênio: "))
                    plano = input("Informe o plano do convênio: ")
                                    
                    convenio = Convenio(empresa, numero, plano, )
                    session.add(convenio)

                    paciente = Paciente(nome=nome, cpf=cpf, rg=rg, idade=idade, convenio=convenio)
                    session.add(paciente)

                    session.commit()
                    print("Paciente cadastrado com sucesso.")

            elif pac == 2:
                cpf = int(input("Informe o CPF do paciente a ser atualizado: "))
                paciente = session.query(Paciente).filter_by(cpf=cpf).first()
                paciente.updatePaciente()
                if paciente:
                    paciente.nome = input("Informe o novo nome do paciente: ") or paciente.nome
                    paciente.idade = int(input("Informe a nova idade do paciente: ")) or paciente.idade
                    session.commit()
                    print("Dados do paciente atualizados com sucesso.")
                else:
                    print("Paciente não encontrado.")

            elif pac == 3:
                cpf = int(input("Informe o CPF do paciente: "))
                paciente = session.query(Paciente).filter_by(cpf=cpf).first()
                if paciente:
                    print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, RG: {paciente.rg}, Convênio: {paciente.convenio.empresa}")
                else:
                    print("Paciente não encontrado.")

            elif pac == 4:
                cpf = int(input("Informe o CPF do paciente a ser deletado: "))
                paciente = session.query(Paciente).filter_by(cpf=cpf).first()
                if paciente:
                    session.delete(paciente)
                    session.commit()
                    print("Paciente deletado com sucesso.")
                else:
                    print("Paciente não encontrado.")
            session.close()

        elif cod == 2:  # Operações com Médico
            med = int(input("1. Cadastrar Médico\n2. Alterar Dados de Médico\n3. Pegar Dados do Médico\n4. Deletar Médico\n"))
            engine, session = get_session()

            if med == 1:
                crm = int(input("Informe o CRM do médico: "))
                medico_existente = session.query(Medico).filter_by(crm=crm).first()
                if medico_existente:
                    print("Médico já cadastrado.")
                else:
                    nome = input("Informe o nome do médico: ")
                    especialidade = input("Informe a especialidade do médico: ")
                    medico = Medico(crm=crm, nome=nome, especialidade=especialidade)
                    session.add(medico)
                    session.commit()
                    print("Médico cadastrado com sucesso.")

            elif med == 2:
                crm = int(input("Informe o CRM do médico a ser atualizado: "))
                medico = session.query(Medico).filter_by(crm=crm).first()
                if medico:
                    medico.nome = input("Informe o novo nome do médico: ") or medico.nome
                    medico.especialidade = input("Informe a nova especialidade do médico: ") or medico.especialidade
                    session.commit()
                    print("Dados do médico atualizados com sucesso.")
                else:
                    print("Médico não encontrado.")

            elif med == 3:
                crm = int(input("Informe o CRM do médico: "))
                medico = session.query(Medico).filter_by(crm=crm).first()
                if medico:
                    print(f"Nome: {medico.nome}, Especialidade: {medico.especialidade}")
                else:
                    print("Médico não encontrado.")

            elif med == 4:
                crm = int(input("Informe o CRM do médico a ser deletado: "))
                medico = session.query(Medico).filter_by(crm=crm).first()
                if medico:
                    session.delete(medico)
                    session.commit()
                    print("Médico deletado com sucesso.")
                else:
                    print("Médico não encontrado.")
            session.close()

        elif cod == 3:  # Fila de Atendimento
            atd = int(input("1. Cadastrar Senha\n2. Gerar novo atendimento\n"))
            engine, session = get_session()

            if atd == 1:
                cpf = int(input('Informe o cpf do paciente: '))
                paciente = session.query(Paciente).filter_by(cpf=cpf).first()
                print("Criando nova senha...")
                if paciente:
                    sen = fila.criarSenha(paciente, session)
                    fila.enfileira(sen)
            
            elif atd == 2:
                senha = fila.desenfileira()
                paciente = senha.paciente

            session.close()

        elif cod == 4:  # Operações com Consultório
            cons = int(input("1. Cadastrar Consultório\n2. Alterar Dados do Consultório\n3. Pegar Dados do Consultório\n4. Deletar Consultório\n"))
            engine, session = get_session()

            if cons == 1:
                numero = int(input("Informe o número do consultório: "))
                consultorio_existente = session.query(Consultorio).filter_by(numero=numero).first()
                if consultorio_existente:
                    print("Consultório já cadastrado.")
                else:
                    localizacao = input("Informe a localização do consultório: ")
                    consultorio = Consultorio(numero=numero, localizacao=localizacao)
                    session.add(consultorio)
                    session.commit()
                    print("Consultório cadastrado com sucesso.")

            elif cons == 2:
                numero = int(input("Informe o número do consultório a ser atualizado: "))
                consultorio = session.query(Consultorio).filter_by(numero=numero).first()
                if consultorio:
                    consultorio.localizacao = input("Informe a nova localização do consultório: ") or consultorio.localizacao
                    session.commit()
                    print("Dados do consultório atualizados com sucesso.")
                else:
                    print("Consultório não encontrado.")

            elif cons == 3:
                numero = int(input("Informe o número do consultório: "))
                consultorio = session.query(Consultorio).filter_by(numero=numero).first()
                if consultorio:
                    print(f"Número: {consultorio.numero}, Localização: {consultorio.localizacao}")
                else:
                    print("Consultório não encontrado.")

            elif cons == 4:
                numero = int(input("Informe o número do consultório a ser deletado: "))
                consultorio = session.query(Consultorio).filter_by(numero=numero).first()
                if consultorio:
                    session.delete(consultorio)
                    session.commit()
                    print("Consultório deletado com sucesso.")
                else:
                    print("Consultório não encontrado.")
            session.close()

        elif cod == 0:
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

            
main()
