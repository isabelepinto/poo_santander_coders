class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        # self.idade = idade - não precisa da idade - tem que ser a data de nascimento


class Medicamento:
    def __init__(self, nome, fabricante, descricao, tipo, preco=0.0):
        self.nome = nome
        self.fabricante = fabricante
        self.descricao = descricao
        self.tipo = tipo
        self.preco = preco


class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome, fabricante, descricao, preco=0.0):
        super().__init__(nome, fabricante, descricao, "Fitoterápico", preco)


class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, fabricante, descricao, preco=0.0, vendido_com_receita=True):
        super().__init__(nome, fabricante, descricao, "Quimioterápico", preco)
        self.vendido_com_receita = vendido_com_receita

    def precisa_receita(self):
        return self.vendido_com_receita
    
class Farmacia:
    def __init__(self):
        self.clientes = {}
        self.medicamentos = []

    def cadastrar_cliente(self, nome, cpf, endereco, telefone, data_nascimento):
        if cpf not in self.clientes:
            cliente = Cliente(nome, cpf, data_nascimento, endereco, telefone)
            self.clientes[cpf] = cliente
            print(f'Cliente {nome} cadastrado com sucesso!')
        else:
            print('CPF já cadastrado.')

    def buscar_cliente(self, cpf):
        if cpf in self.clientes:
            cliente = self.clientes[cpf]
            print(f'Nome: {cliente.nome}')
            print(f'CPF: {cliente.cpf}')
            print(f'Endereço: {cliente.endereco}')
            print(f'Telefone: {cliente.telefone}')
        else:
            print('Cliente não encontrado.')

    def cadastrar_medicamento_fitoterapico(self, nome, fabricante, descricao, preco=0.0):
        medicamento = MedicamentoFitoterapico(nome, fabricante, descricao, preco)
        self.medicamentos.append(medicamento)
        print(f'Medicamento fitoterápico {nome} cadastrado com sucesso!')

    def cadastrar_medicamento_quimioterapico(self, nome, fabricante, descricao, preco=0.0):
        medicamento = MedicamentoQuimioterapico(nome, fabricante, descricao, preco)
        self.medicamentos.append(medicamento)
        print(f'Medicamento quimioterápico {nome} cadastrado com sucesso!')

    def buscar_medicamento(self, termo_busca):
        resultados = []
        for medicamento in self.medicamentos:
            if (termo_busca in medicamento.nome) or (termo_busca in medicamento.fabricante) or (termo_busca in medicamento.descricao):
                resultados.append(medicamento)

        if resultados:
            for medicamento in resultados:
                print('---')
                print(f'Nome: {medicamento.nome}')
                print(f'Fabricante: {medicamento.fabricante}')
                print(f'Descrição: {medicamento.descricao}')
                print(f'Tipo: {medicamento.tipo}')
                if medicamento.tipo == 'Quimioterápico':
                    receita = 'Sim' if medicamento.vendido_com_receita else 'Não'
                    print(f'Requer receita: {receita}')
        else:
            print('Nenhum medicamento encontrado.')
            
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
                                    print('Venda cancelada. Receita não verificada.')
                                    return

            cliente = self.clientes[cpf_cliente]

            if cliente.data_nascimento[-4:] <= '1956':
                total *= 0.8

            if total > 150:
                total *= 0.9

            print(f'Cliente: {cliente.nome}')
            print(f'Total antes dos descontos: R$ {total + 0:.2f}')
            print(f'Desconto aplicado: R$ {total * 0.1:.2f}')
            print(f'Total a pagar: R$ {total:.2f}')
        else:
            print('Cliente não encontrado.')

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

    def emitir_relatorio_medicamentos(self):
        print('--- Relatório de Medicamentos ---')
        medicamentos_ordenados = sorted(
            self.medicamentos, key=lambda medicamento: medicamento.nome)
        for medicamento in medicamentos_ordenados:
            print('---')
            print(f'Nome: {medicamento.nome}')
            print(f'Fabricante: {medicamento.fabricante}')
            print(f'Descrição: {medicamento.descricao}')
            print(f'Tipo: {medicamento.tipo}')
            if medicamento.tipo == 'Quimioterápico':
                receita = 'Sim' if medicamento.vendido_com_receita else 'Não'
                print(f'Requer receita: {receita}')
                
    def emitir_relatorio_atendimentos(self, remedio_mais_vendido):
        print('--- Relatório de Atendimentos do Dia ---')
        print(
            f'Remédio mais vendido: {remedio_mais_vendido} (Quantidade: {quantidade_atendimentos[remedio_mais_vendido]}, Valor Total: R$ {quantidade_atendimentos[remedio_mais_vendido]:.2f})')
        print(f'Quantidade de pessoas atendidas: {len(self.clientes)}')


# Função para exibir o menu e interagir com o usuário
def exibir_menu():
    print('--- Menu ---')
    print('1 - Cadastrar cliente')
    print('2 - Buscar cliente por CPF')
    print('3 - Cadastrar medicamento fitoterápico')
    print('4 - Cadastrar medicamento quimioterápico')
    print('5 - Buscar medicamento por termo')
    print('6 - Realizar venda')
    print('7 - Emitir relatórios')
    print('8 - Sair')


# Instanciando a farmácia
farmacia = Farmacia()

# Loop principal
remedio_mais_vendido = None

while True:
    exibir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do cliente: ')
        cpf = input('CPF do cliente (apenas números): ')
        endereco = input('Endereço do cliente: ')
        telefone = input('Telefone do cliente: ')
        data_nascimento = input('Data de nascimento do cliente (DD/MM/AAAA): ')
        farmacia.cadastrar_cliente(nome, cpf, endereco, telefone, data_nascimento)
    elif opcao == '2':
        cpf = input('Digite o CPF do cliente para buscar: ')
        farmacia.buscar_cliente(cpf)
    elif opcao == '3':
        nome = input('Nome do medicamento fitoterápico: ')
        fabricante = input('Fabricante do medicamento: ')
        descricao = input('Descrição do medicamento: ')
        preco = float(input('Preço do medicamento: '))
        farmacia.cadastrar_medicamento_fitoterapico(nome, fabricante, descricao, preco)
    elif opcao == '4':
        nome = input('Nome do medicamento quimioterápico: ')
        fabricante = input('Fabricante do medicamento: ')
        descricao = input('Descrição do medicamento: ')
        preco = float(input('Preço do medicamento: '))
        vendido_com_receita = input('Vendido com receita (S/N): ').lower() == 's'
        farmacia.cadastrar_medicamento_quimioterapico(nome, fabricante, descricao, preco, vendido_com_receita)
    elif opcao == '5':
        termo_busca = input('Digite o termo de busca: ')
        farmacia.buscar_medicamento(termo_busca)
    elif opcao == '6':
        cpf_cliente = input('Digite o CPF do cliente: ')
        num_medicamentos = int(input('Quantidade de medicamentos a serem vendidos: '))
        lista_medicamentos = []
        for i in range(num_medicamentos):
            nome_medicamento = input(f'Nome do medicamento {i + 1}: ')
            lista_medicamentos.append(Medicamento(nome_medicamento, '', '', ''))

        farmacia.realizar_venda(cpf_cliente, lista_medicamentos)
    elif opcao == '7':
        farmacia.emitir_relatorio_clientes()
        farmacia.emitir_relatorio_medicamentos()
        farmacia.emitir_relatorio_atendimentos(remedio_mais_vendido)
    elif opcao == '8':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Escolha novamente.')