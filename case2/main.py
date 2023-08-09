# Como representar um cliente de banco e uma conta bancária em Python, onde toda conta possui um cliente e vice-versa.

class Cliente:
    def __init__(self, nome, conta) -> None:
        self.nome = nome    
        self.conta = conta


class Conta:
    def __init__(self, cliente, conta) -> None:
        self.cliente = cliente
        self.conta = conta
        
        

isabele = Cliente('isabele', 25)

print(isabele.nome, isabele.conta)