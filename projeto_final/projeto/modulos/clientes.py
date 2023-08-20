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