from modulos import clientes
from modulos import laboratorios
from modulos import medicamentos
from modulos import farmacias

# Função para exibir o menu de opções

def exibir_menu():
    print('--- Menu ---')
    print('1 - Cadastrar cliente')
    print('2 - Buscar cliente por CPF')
    print('3 - Cadastrar medicamento fitoterápico')
    print('4 - Cadastrar medicamento quimioterápico')
    print('5 - Cadastrar laboratório')
    print('6 - Exibir lista medicamentos')
    print('7 - Buscar medicamento por termo')
    print('8 - Realizar venda')
    print('9 - Emitir relatórios')
    print('10 - Sair')


# Cria uma instância da classe Farmacia
farmacia = farmacias.Farmacia()


# cria instâncias de laboratórios e os adiciona ao dicionario de laboratórios da farmácia


laboratorio1 = laboratorios.Laboratorio("cbd", "travessa 1", "21922222222","rio de janeiro", "rio de janeiro")
laboratorio2 = laboratorios.Laboratorio("abc", "travessa 2", "11933333333","são paulo", "são paulo")
laboratorio3 = laboratorios.Laboratorio("cbd", "travessa 2", "81944444444", "recife", "pernambuco")

farmacia.laboratorios.append(laboratorio1)
farmacia.laboratorios.append(laboratorio2)
farmacia.laboratorios.append(laboratorio3)


# Cria instâncias de medicamentos fitoterápicos e quimioterápicos e os adiciona à lista de medicamentos da farmácia
medicamento_fitoterapico1 = medicamentos.MedicamentoFitoterapico("Chá de Camomila", laboratorio1, "Infusão de flores de camomila", 5.0)
medicamento_fitoterapico2 = medicamentos.MedicamentoFitoterapico("Xarope de Guaco", laboratorio1, "Xarope expectorante de guaco", 15.0)
farmacia.medicamentos.append(medicamento_fitoterapico1)
farmacia.medicamentos.append(medicamento_fitoterapico2)

medicamento_quimioterapico1 = medicamentos.MedicamentoQuimioterapico("Imatinibe", laboratorio2, "Agente quimioterápico", 50.0, True)
medicamento_quimioterapico2 = medicamentos.MedicamentoQuimioterapico("Procarbazina", laboratorio3, "Agente quimioterápico", 75.0, False)
medicamento_quimioterapico3 = medicamentos.MedicamentoQuimioterapico("Abiraterona", laboratorio3, "Agente quimioterápico", 65.0, False)
medicamento_quimioterapico4 = medicamentos.MedicamentoQuimioterapico("Taxanos", laboratorio2, "Agente quimioterápico", 80.0, True)
farmacia.medicamentos.append(medicamento_quimioterapico1)
farmacia.medicamentos.append(medicamento_quimioterapico2)
farmacia.medicamentos.append(medicamento_quimioterapico3)
farmacia.medicamentos.append(medicamento_quimioterapico4)

# Cria instâncias de clientes e os adiciona ao dicionário de clientes da farmácia
cliente1 = clientes.Cliente("Leôncio", "12345678900", "01/01/1957","Rua A, 123", "1234567890")
cliente2 = clientes.Cliente("isaac", "98765432100", "15/05/1995","Avenida B, 456", "9876543210")
cliente3 = clientes.Cliente("isabele", "54321123456", "30/11/2000","Praça C, 789", "5432167890")
cliente4 = clientes.Cliente("Caroline", "65432101234", "30/11/1998","Praça C, 789", "5432167890")
cliente5 = clientes.Cliente("Guilherme", "87654321012", "30/11/1995","Praça C, 789", "5432167890")
farmacia.clientes[cliente1.cpf] = cliente1
farmacia.clientes[cliente2.cpf] = cliente2
farmacia.clientes[cliente3.cpf] = cliente3
farmacia.clientes[cliente4.cpf] = cliente4
farmacia.clientes[cliente5.cpf] = cliente5


# Variável para armazenar o nome do medicamento mais vendido
remedio_mais_vendido = None

# Loop principal do programa
while True:
    # Exibe o menu de opções
    exibir_menu()
    opcao = input('Escolha uma opção: ')

    # Verifica a opção escolhida pelo usuário e executa a funcionalidade correspondente
    if opcao == '1':
        # Opção para cadastrar um novo cliente
        nome = input('Nome do cliente: ')
        cpf = input('CPF do cliente (apenas números): ')
        endereco = input('Endereço do cliente: ')
        telefone = input('Telefone do cliente: ')
        data_nascimento = input('Data de nascimento do cliente (DD/MM/AAAA): ')
        farmacia.cadastrar_cliente(
            nome, cpf, endereco, telefone, data_nascimento)
    elif opcao == '2':
        # Opção para buscar um cliente por CPF
        cpf = input('CPF do cliente (apenas números): ')
        farmacia.buscar_cliente(cpf)
    elif opcao == '3':
        # Opção para cadastrar um novo medicamento fitoterápico
        nome = input('Nome do medicamento fitoterápico: ')
        laboratorio_nome = input('Nome do laboratório do medicamento: ')
        descricao = input('Descrição do medicamento: ')
        preco = float(input('Preço do medicamento: '))
        farmacia.cadastrar_medicamento_fitoterapico(
            nome, laboratorio_nome, descricao, preco)
    elif opcao == '4':
        # Opção para cadastrar um novo medicamento quimioterápico
        nome = input('Nome do medicamento quimioterápico: ')
        laboratorio_nome = input('Nome do laboratório do medicamento: ')
        descricao = input('Descrição do medicamento: ')
        preco = float(input('Preço do medicamento: '))
        vendido_com_receita = input(
            'O medicamento requer receita médica? (S/N): ').lower() == 's'
        farmacia.cadastrar_medicamento_quimioterapico(
            nome, laboratorio_nome, descricao, preco, vendido_com_receita)
    elif opcao == '5':
        # Opção para cadastrar laboratório
        nome = input('Nome do laboratório: ')
        endereco = input('Endereço do laboratório: ')
        telefone = input('Telefone para contato: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        farmacia.cadastrar_laboratorio(
            nome, endereco, telefone, cidade, estado)
    elif opcao == '6':
        # Opção para exibir a lista de medicamentos cadastrados
        farmacia.exibir_medicamentos_cadastrados()
    elif opcao == '7':
        # Opção para buscar medicamentos por termo
        termo_busca = input('Digite o termo de busca: ')
        farmacia.buscar_medicamento(termo_busca)
    elif opcao == '8':
        # Opção para realizar uma venda
        cpf_cliente = input('CPF do cliente (apenas números): ')
        lista_medicamentos = []
        while True:
            nome_medicamento = input(
                'Nome do medicamento (ou "fim" para encerrar a lista): ')
            if nome_medicamento.lower() == 'fim':
                break
            lista_medicamentos.append(
                medicamentos.Medicamento(nome_medicamento, "", "", ""))
        farmacia.realizar_venda(cpf_cliente, lista_medicamentos)
    elif opcao == '9':
        # Opção para emitir relatórios
        print('--- Opções de Relatórios ---')
        print('1 - Relatório de Clientes Cadastrados')
        print('2 - Relatório de Medicamentos Cadastrados')
        print('3 - Relatório de Atendimentos do Dia')
        relatorio_opcao = input('Escolha uma opção de relatório: ')
        if relatorio_opcao == '1':
            farmacia.emitir_relatorio_clientes()
        elif relatorio_opcao == '2':
            farmacia.emitir_relatorio_medicamentos()
        elif relatorio_opcao == '3':
           # remedio_mais_vendido = input(
              #  'Digite o nome do medicamento mais vendido (ou deixe em branco): ')
            #farmacia.emitir_relatorio_atendimentos(remedio_mais_vendido)
            farmacia.emitir_relatorio_atendimentos()

        else:
            print('Opção inválida.')
    elif opcao == '10':
        print('Saindo...')

        break
    else:
        print('Opção inválida. Digite um número de 1 a 10.')
