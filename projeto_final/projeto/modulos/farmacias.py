from modulos import laboratorios
from modulos import clientes
from modulos import medicamentos


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
            cliente = clientes.Cliente(nome, cpf, data_nascimento, endereco, telefone)
            self.clientes[cpf] = cliente
            print(f'Cliente {nome} cadastrado com sucesso!')
        else:
            print('CPF já cadastrado.')

    # Método para cadastrar um novo laboratório
    def cadastrar_laboratorio(self, nome, endereco, telefone, cidade, estado):
        laboratorio = laboratorios.Laboratorio(nome, endereco, telefone, cidade, estado)
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
            medicamento = medicamentos.MedicamentoFitoterapico(
                nome, laboratorio, descricao, preco)
            self.medicamentos.append(medicamento)
            print(f'Medicamento fitoterápico {nome} cadastrado com sucesso!')
        else:
            print('Laboratório não encontrado.')

    # Método para cadastrar um novo medicamento quimioterapico na farmácia
    def cadastrar_medicamento_quimioterapico(self, nome, laboratorio_nome, descricao, preco=0.0, vendido_com_receita=True):
        laboratorio = self.buscar_laboratorio(laboratorio_nome)
        if laboratorio:
            medicamento = medicamentos.MedicamentoQuimioterapico(
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
            if isinstance(medicamento, medicamentos.MedicamentoQuimioterapico):
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

                        if isinstance(estoque_medicamento, medicamentos.MedicamentoQuimioterapico):
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