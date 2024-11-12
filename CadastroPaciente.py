from Paciente import Paciente, Convenio
from Banco import sessionmaker
from Banco import create_engine


class CadastroSenha:

    nossobanco = create_engine('sqlite:///banco/medcare.db')
    Session = sessionmaker(bind=nossobanco)

    def main(self):
        cpf = input('Informe o cpf do paciente: ')

        # Verificar cpf no banco
        status = self.verifyCPF(cpf)
        session = self.Session()

        if not status:
            print('Paciente sem cadastro\nRealize o cadastro do Paciente...')

            print('\nCadastro de Convenio')
            empresa = input('Informe a empresa: ')
            numero = input('Informe o numero do convenio: ')
            plano = input('Informe o plano do convenio:')

            convenio = Convenio(empresa, numero, plano)
            session.add(convenio)

            print('Cadastro de Paciente')
            nome = input('Informe o Nome do Paciente: ')
            rg = input('Informe o RG: ')
            idade = input('Idade do paciente: ')

            paciente = Paciente(nome, cpf, rg, idade, convenio)
            session.add(paciente)

            session.commit()  # Salva as alterações no banco
            print(f'paciete {paciente.nome} foi cadastrado!!')
            print(f'Convenio {convenio.empresa} {convenio.plano} cadastrado com sucesso!')

            # Cadastrar usuário
            # Pega os dados do paciente

            senha = self.criar_senha(session)
            print(f'Senha gerada para o paciente {paciente.nome}: {senha}')

        else:
            # pelo que eu entendi não precisa usar o get aqui o First faz a busca com o cpf que nós fornecemos e retorna os dados
            paciente = session.query(Paciente).filter_by(cpf=cpf).first()

            if paciente:
                # Exibe os dados do paciente
                print(f"Dados do paciente encontrado:")
                print(f"Nome: {paciente.nome}")
                print(f"CPF: {paciente.cpf}")
                print(f"RG: {paciente.rg}")
                print(f"Idade: {paciente.idade}")

                # Perguntar se deseja gerar uma senha
                gerar_senha = input( 'Deseja gerar uma senha para o paciente? (s/n): ').strip().lower()

                if gerar_senha == 's':
                    # Criar uma nova senha para o paciente
                    senha = self.criar_senha(session)
                    print(f'Senha gerada para o Paciente {paciente.nome}: {senha}')
                else:
                    print(f"Senha não gerada para o Paciente {paciente.nome}.")
            else:
                print("Paciente não encontrado no banco.")

        session.close()

    

        # Aloca o Paciente a senha, falta isso

        # Criar numero da senha, foi feito

        # Joga a senha na fila (ultimo) (Adicionar ao Banco), foi feito mas vamos verificar

    def verifyCPF(self, cpf):
        session = self.Session()  # Cria uma nova sessão
        existe = session.query(Paciente).filter_by(cpf=cpf).first() is not None
        session.close()  # Fecha a sessão para liberar recursos
        print(existe)

        return existe
        
