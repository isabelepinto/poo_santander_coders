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



