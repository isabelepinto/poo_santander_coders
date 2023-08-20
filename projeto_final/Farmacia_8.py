# Importa a classe datetime para manipulação de datas
from datetime import datetime

# Definição da classe Cliente


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco, telefone):
        # Inicializa os atributos do cliente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone

    # Método para calcular a idade do cliente com base na data de nascimento
    def calcular_idade(self):
        data_nascimento = datetime.strptime(self.data_nascimento, '%d/%m/%Y')
        hoje = datetime.now()
        idade = hoje.year - data_nascimento.year - \
            ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade

# Definição da classe Medicamento


class Medicamento:
    def __init__(self, nome, laboratorio, descricao, tipo, preco=0.0):
        # Inicializa os atributos do medicamento
        self.nome = nome
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.tipo = tipo
        self.preco = preco

# Definição da classe MedicamentoFitoterapico, derivada de Medicamento


class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome, laboratorio, descricao, preco=0.0):
        # Chama o construtor da classe pai (Medicamento) e define o tipo como "Fitoterápico"
        super().__init__(nome, laboratorio, descricao, "Fitoterápico", preco)

# Definição da classe MedicamentoQuimioterapico, derivada de Medicamento


class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, laboratorio, descricao, preco=0.0, vendido_com_receita=True):
        # Chama o construtor da classe pai (Medicamento) e define o tipo como "Quimioterápico"
        super().__init__(nome, laboratorio, descricao, "Quimioterápico", preco)
        self.vendido_com_receita = vendido_com_receita

    # Método para verificar se o medicamento quimioterápico precisa de receita
    def precisa_receita(self):
        return self.vendido_com_receita

 # Definição da classe LABORATÓRIO


class Laboratorio:
    def __init__(self, nome, endereco, telefone, cidade, estado):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

# Definição da classe Farmacia


class Farmacia:
    def __init__(self):
        # Inicializa os dicionários para clientes e medicamentos, e o dicionário de quantidade de atendimentos
        self.clientes = {}
        self.medicamentos = []
        self.quantidade_atendimentos = {}
        self.laboratorios = []
        self.medicamentos_vendidos = {}


    # Método para cadastrar um novo cliente na farmácia
    def cadastrar_cliente(self, nome, cpf, endereco, telefone, data_nascimento):
        if cpf not in self.clientes:
            cliente = Cliente(nome, cpf, data_nascimento, endereco, telefone)
            self.clientes[cpf] = cliente
            print(f'Cliente {nome} cadastrado com sucesso!')
        else:
            print('CPF já cadastrado.')

    # Método para cadastrar um novo laboratório
    def cadastrar_laboratorio(self, nome, endereco, telefone, cidade, estado):
        laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
        self.laboratorios.append(laboratorio)
        print(f'Laboratório {nome} cadastrado com sucesso!')

    # Método para buscar e exibir informações de um cliente pelo CPF
    def buscar_cliente(self, cpf):
        if cpf in self.clientes:
            cliente = self.clientes[cpf]
            print(f'Nome: {cliente.nome}')
            print(f'CPF: {cliente.cpf}')
            print(f'Endereço: {cliente.endereco}')
            print(f'Telefone: {cliente.telefone}')
        else:
            print('Cliente não encontrado.')

    # Método para cadastrar um novo medicamento fitoterápico na farmácia
    def cadastrar_medicamento_fitoterapico(self, nome, laboratorio_nome, descricao, preco=0.0):
        laboratorio = self.buscar_laboratorio(laboratorio_nome)
        if laboratorio:
            medicamento = MedicamentoFitoterapico(
                nome, laboratorio, descricao, preco)
            self.medicamentos.append(medicamento)
            print(f'Medicamento fitoterápico {nome} cadastrado com sucesso!')
        else:
            print('Laboratório não encontrado.')

    # Método para cadastrar um novo medicamento quimioterapico na farmácia
    def cadastrar_medicamento_quimioterapico(self, nome, laboratorio_nome, descricao, preco=0.0, vendido_com_receita=True):
        laboratorio = self.buscar_laboratorio(laboratorio_nome)
        if laboratorio:
            medicamento = MedicamentoQuimioterapico(
                nome, laboratorio, descricao, preco, vendido_com_receita)
            self.medicamentos.append(medicamento)
            print(f'Medicamento quimioterápico {nome} cadastrado com sucesso!')
        else:
            print('Laboratório não encontrado.')

    # Método para buscar laboratórios com base em um nome
    def buscar_laboratorio(self, nome_laboratorio):
        for laboratorio in self.laboratorios:
            if laboratorio.nome == nome_laboratorio:
                return laboratorio
        return None

    # Método para exibir a lista de medicamentos cadastrados na farmácia
    def exibir_medicamentos_cadastrados(self):
        print('--- Medicamentos Cadastrados ---')
        for medicamento in self.medicamentos:
            print('---')
            print(f'Nome: {medicamento.nome}')
            print(f'laboratório: {medicamento.laboratorio.nome}')
            print(f'Descrição: {medicamento.descricao}')
            print(f'Tipo: {medicamento.tipo}')
            if isinstance(medicamento, MedicamentoQuimioterapico):
                receita = 'Sim' if medicamento.vendido_com_receita else 'Não'
                print(f'Requer receita: {receita}')

    # Método para buscar medicamentos com base em um termo de busca
    def buscar_medicamento(self, termo_busca):
        resultados = []
        for medicamento in self.medicamentos:
            if (termo_busca in medicamento.nome) or (termo_busca in medicamento.laboratorio.nome) or (termo_busca in medicamento.descricao):
                resultados.append(medicamento)

        if resultados:
            for medicamento in resultados:
                print('---')
                print(f'Nome: {medicamento.nome}')
                print(f'laboratório: {medicamento.laboratorio.nome}')
                print(f'Descrição: {medicamento.descricao}')
                print(f'Tipo: {medicamento.tipo}')
                if medicamento.tipo == 'Quimioterápico':
                    receita = 'Sim' if medicamento.vendido_com_receita else 'Não'
                    print(f'Requer receita: {receita}')
        else:
            print('Nenhum medicamento encontrado.')

    # Método para realizar uma venda de medicamentos para um cliente
    def realizar_venda(self, cpf_cliente, lista_medicamentos):
        if cpf_cliente in self.clientes:
            total = 0
            tem_receita_controlado = False
            nome_remedio_controlado = None

            for medicamento in lista_medicamentos:
                for estoque_medicamento in self.medicamentos:
                    if estoque_medicamento.nome == medicamento.nome:
                        total += estoque_medicamento.preco

                        if isinstance(estoque_medicamento, MedicamentoQuimioterapico):
                            if estoque_medicamento.precisa_receita():
                                tem_receita_controlado = True
                                nome_remedio_controlado = estoque_medicamento.nome
                                resposta = input(
                                    f'O remédio "{nome_remedio_controlado}" é controlado. Verificou a receita? (S/N): ')
                                if resposta.lower() != 's':
                                    print(
                                        'Venda cancelada. Receita não verificada.')
                                    return

            
            
            
            cliente = self.clientes[cpf_cliente]
            idade_cliente = cliente.calcular_idade()

            print(f'Cliente: {cliente.nome}')
            print(f'Total antes dos descontos: R$ {total :.2f}')

            if idade_cliente > 65:
                desconto_65= total*0.2
            else:
                desconto_65=0

            if total > 150:
                desconto_150 = total*0.1
            else:
                desconto_150 = 0
            #recalculo do total
            total = total - (desconto_150+desconto_65)
            print(f'Desconto aplicado: R$ {desconto_150+desconto_65:.2f}')
            print(f'Total a pagar: R$ {total:.2f}') 

            for medicamento in lista_medicamentos:
                if medicamento.nome in self.medicamentos_vendidos:
                    self.medicamentos_vendidos[medicamento.nome] += 1
                else:
                    self.medicamentos_vendidos[medicamento.nome] = 1

            if cliente.nome in self.quantidade_atendimentos.keys():
                self.quantidade_atendimentos[cliente.nome]+=1
            else:
                self.quantidade_atendimentos[cliente.nome]=1
        else:
            print('Cliente não encontrado.')

    # Método para emitir um relatório de clientes cadastrados
    def emitir_relatorio_clientes(self):
        print('--- Relatório de Clientes ---')
        clientes_ordenados = sorted(
            self.clientes.values(), key=lambda cliente: cliente.nome)
        for cliente in clientes_ordenados:
            print('---')
            print(f'Nome: {cliente.nome}')
            print(f'CPF: {cliente.cpf}')
            print(f'Endereço: {cliente.endereco}')
            print(f'Telefone: {cliente.telefone}')

    # Método para emitir um relatório de medicamentos cadastrados
    def emitir_relatorio_medicamentos(self):
        print('--- Relatório de Medicamentos ---')
        medicamentos_ordenados = sorted(
            self.medicamentos, key=lambda medicamento: medicamento.nome)
        for medicamento in medicamentos_ordenados:
            print('---')
            print(f'Nome: {medicamento.nome}')
            print(f'laboratório: {medicamento.laboratorio.nome}')
            print(f'Descrição: {medicamento.descricao}')
            print(f'Tipo: {medicamento.tipo}')
            if medicamento.tipo == 'Quimioterápico':
                receita = 'Sim' if medicamento.vendido_com_receita else 'Não'
                print(f'Requer receita: {receita}')
        

    # Método para emitir um relatório de atendimentos do dia


    def emitir_relatorio_atendimentos(self):
        print('--- Relatório de Atendimentos do Dia ---')
    
        if self.medicamentos_vendidos:
            remedio_mais_vendido = max(self.medicamentos_vendidos, key=self.medicamentos_vendidos.get)
            quantidade_mais_vendido = self.medicamentos_vendidos[remedio_mais_vendido]
            valor_total_mais_vendido = 0.0

            for medicamento in self.medicamentos:
                if medicamento.nome == remedio_mais_vendido:
                    valor_total_mais_vendido = quantidade_mais_vendido * medicamento.preco
                    break

            print(f'Remédio mais vendido: {remedio_mais_vendido} (Quantidade: {quantidade_mais_vendido}, Valor Total: R$ {valor_total_mais_vendido:.2f})')




        else:
            print('Nenhum atendimento realizado.')
        print(f'Quantidade de pessoas atendidas: {sum(self.quantidade_atendimentos.values())}')

    # Método para buscar o preço de um medicamento pelo nome

    def buscar_preco_medicamento(self, nome_medicamento):
        for medicamento in self.medicamentos:
            if medicamento.nome == nome_medicamento:
                return medicamento.preco
        return "Opção inválida"

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
farmacia = Farmacia()


# cria instâncias de laboratórios e os adiciona ao dicionario de laboratórios da farmácia


laboratorio1 = Laboratorio("cbd", "travessa 1", "21922222222","rio de janeiro", "rio de janeiro")
laboratorio2 = Laboratorio("abc", "travessa 2", "11933333333","são paulo", "são paulo")
laboratorio3 = Laboratorio("cbd", "travessa 2", "81944444444", "recife", "pernambuco")

farmacia.laboratorios.append(laboratorio1)
farmacia.laboratorios.append(laboratorio2)
farmacia.laboratorios.append(laboratorio3)


# Cria instâncias de medicamentos fitoterápicos e quimioterápicos e os adiciona à lista de medicamentos da farmácia
medicamento_fitoterapico1 = MedicamentoFitoterapico("Chá de Camomila", laboratorio1, "Infusão de flores de camomila", 5.0)
medicamento_fitoterapico2 = MedicamentoFitoterapico("Xarope de Guaco", laboratorio1, "Xarope expectorante de guaco", 15.0)
farmacia.medicamentos.append(medicamento_fitoterapico1)
farmacia.medicamentos.append(medicamento_fitoterapico2)

medicamento_quimioterapico1 = MedicamentoQuimioterapico("Imatinibe", laboratorio2, "Agente quimioterápico", 50.0, True)
medicamento_quimioterapico2 = MedicamentoQuimioterapico("Procarbazina", laboratorio3, "Agente quimioterápico", 75.0, False)
medicamento_quimioterapico3 = MedicamentoQuimioterapico("Abiraterona", laboratorio3, "Agente quimioterápico", 65.0, False)
medicamento_quimioterapico4 = MedicamentoQuimioterapico("Taxanos", laboratorio2, "Agente quimioterápico", 80.0, True)
farmacia.medicamentos.append(medicamento_quimioterapico1)
farmacia.medicamentos.append(medicamento_quimioterapico2)
farmacia.medicamentos.append(medicamento_quimioterapico3)
farmacia.medicamentos.append(medicamento_quimioterapico4)

# Cria instâncias de clientes e os adiciona ao dicionário de clientes da farmácia
cliente1 = Cliente("Leôncio", "12345678900", "01/01/1957","Rua A, 123", "1234567890")
cliente2 = Cliente("isaac", "98765432100", "15/05/1995","Avenida B, 456", "9876543210")
cliente3 = Cliente("isabele", "54321123456", "30/11/2000","Praça C, 789", "5432167890")
cliente4 = Cliente("Caroline", "65432101234", "30/11/1998","Praça C, 789", "5432167890")
cliente5 = Cliente("Guilherme", "87654321012", "30/11/1995","Praça C, 789", "5432167890")
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
                Medicamento(nome_medicamento, "", "", ""))
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
