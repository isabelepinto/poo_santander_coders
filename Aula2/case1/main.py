# Como representar uma fração em Python utilizando classes, com métodos representando as diferentes operações entre frações.
class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador
       
    """_summary_
    
    Função para fazer diferentes operações entre frações e retornar o numerador e denominador do resultado entre elas
    
    Args:
        numerador(int) -> o numerador da fração 
        denominador(int) -> o denominador da fração
    """
        
    def adicionar(self, fracao):
        numerador = self.numerador * fracao.denominador + self.denominador * fracao.numerador
        denominador = self.denominador * fracao.denominador
        
        return Fracao(numerador, denominador)
    
    
    def subtrair(self, fracao):
        numerador = self.numerador * fracao.denominador - self.denominador * fracao.numerador
        denominador = self.denominador * fracao.denominador
        
        return Fracao(numerador, denominador)
    
    
    def multiplicar(self, fracao):
        numerador = self.numerador * fracao.numerador
        denominador = self.denominador * fracao.denominador
        
        return Fracao(numerador, denominador)
    
    
    def dividir(self, fracao):
        numerador = self.numerador * fracao.denominador
        denominador = self.denominador * fracao.numerador
        
        return Fracao(numerador, denominador)
    
    
    def apresenta(self):
        return f'{self.numerador}/{self.denominador}'
    
    
#declarando as frações   
fracao1 = Fracao(int(input('Numerador da Fração 1: ')), int(input('Denominador da Fração 1: ')))
fracao2 = Fracao(int(input('\nNumerador da Fração 2: ')), int(input('Denominador da Fração 2: ')))

#realizando as operações
add = fracao1.adicionar(fracao2).apresenta()
sub = fracao1.subtrair(fracao2).apresenta()
mult = fracao1.multiplicar(fracao2).apresenta()
div = fracao1.dividir(fracao2).apresenta()

print(f'Resultado da adição: {add}')     
print(f'Resultado da subtração: {sub}')     
print(f'Resultado da multiplicação: {mult}')     
print(f'Resultado da divisão: {div}')    