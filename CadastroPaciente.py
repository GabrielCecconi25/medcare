import Paciente

class CadastroSenha:
    def main():
        cpf = input('Informe o cpf do paciente: ')

        # Verificar cpf no banco
        status = verifyCPF(cpf)
        if not(status):
            print('Paciente sem cadastro\nRealize o cadastro do Paciente...')
            
            print('\nCadastro de Convenio')
            empresa = input('Informe a empresa: ')
            numero = input('Informe o numero do convenio: ')
            plano = input('Informe o plano do convenio:')

            convenio = Convenio(empresa, numero, plano)

            print('Cadastro de Paciente')
            nome = input('Informe o Nome do Paciente: ')
            rg = input('Informe o RG: ')
            idade = input('Idade do paciente: ')

            paciente = Paciente(nome, cpf, rg, idade, convenio)


            # Cadastrar usuário
            # Pega os dados do paciente
        else:
            getPaciente(cpf)

            # Pega os dados do paciente
        
        # Cria uma senha para o paciente
        # Aloca o Paciente a senha

        # Criar numero da senha

        # numero da senha = Senha(numero)

        # Joga a senha na fila (ultimo) (Adicionar ao Banco)
        
    def getPaciente(cpf):
        #Script puxar dados do paciente
        convenio = Convenio(empresa, numero, plano)
        paciente = Paciente(nome, cpf, rg, idade, convenio)

    
    def verifyCPF(cpf):
        status = VerificarCPFBANCO()
        return status

    

        
