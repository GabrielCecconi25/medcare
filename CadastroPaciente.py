from Banco import get_session
from Paciente import Paciente
from Convenio import Convenio
from Senha import Senha


class CadastroSenha:

    def main(self):
        cpf = int(input('Informe o cpf do paciente: '))

        # Cria conexão do banco
        engine, session = get_session()
    
        # Verificar cpf no banco
        status = self.verifyCPF(cpf, session)

        if not status:
            print('Paciente sem cadastro\nRealize o cadastro do Paciente...')

            print('\nCadastro de Convenio')
            empresa = input('Informe a empresa: ')
            numero = input('Informe o numero do convenio: ')
            plano = input('Informe o plano do convenio:')

            print('\nCadastro de Paciente')
            nome = input('Informe o Nome do Paciente: ')
            rg = input('Informe o RG: ')
            idade = input('Idade do paciente: ')

            convenio = Convenio(empresa, numero, plano)
            session.add(convenio)

            paciente = Paciente(nome, cpf, rg, idade, convenio)
            session.add(paciente)


            session.commit()  # Salva as alterações no banco
            print(f'paciete {paciente.nome} foi cadastrado!!')
            print(f'Convenio {convenio.empresa} {convenio.plano} cadastrado com sucesso!')

        else:
            paciente = session.query(Paciente).filter_by(cpf=cpf).first()

        if paciente:
            # Exibe os dados do paciente
            print(f"Dados do paciente encontrado:")
            print(f"Nome: {paciente.nome}")
            print(f"CPF: {paciente.cpf}")
            print(f"RG: {paciente.rg}")
            print(f"Idade: {paciente.idade}")

            # Perguntar se deseja gerar uma senha
            gerar_senha = None
            while gerar_senha != 'n' and gerar_senha != 's':
                gerar_senha = input('Deseja gerar uma senha para o paciente? (s/n): ').strip().lower()

            if gerar_senha == 's':
                # Criar uma nova senha para o paciente
                senha = Senha(paciente, session)
                
                session.commit()

                print(f'Senha gerada para o Paciente {paciente.nome}: {senha.numero}')
            else:
                print(f"Senha não gerada para o Paciente {paciente.nome}.")

        # Joga a senha na fila (ultimo) (Adicionar ao Banco), foi feito mas vamos verificar

        #Fecha conexão com o banco
        session.close()

    def verifyCPF(self, cpf, session):
        existe = session.query(Paciente).filter_by(cpf=cpf).first() is not None
        return existe
        


#123456