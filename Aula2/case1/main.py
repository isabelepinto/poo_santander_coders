#Como representar uma fração em Python utilizando classes, com métodos representando as diferentes operações entre frações.
class Fracao:
    """Função para fazer diferentes operações entre frações e retornar o numerador e denominador do resultado entre elas.
    input -> numerador (int), denominador(int)
    """
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
       
        
    def adicionar(self, fracao2):
        numerador = self.numerador * fracao2.denominador + self.denominador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        
        return Fracao(numerador, denominador)
    
    
    def subtrair(self, fracao2):
        numerador = self.numerador * fracao2.denominador - self.denominador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        
        return Fracao(numerador, denominador)
    
    
    def multiplicar(self, fracao2):
        numerador = self.numerador * fracao2.numerador
        denominador = self.denominador * fracao2.denominador
        
        return Fracao(numerador, denominador)
    
    
    def dividir(self, fracao2):
        numerador = self.numerador * fracao2.denominador
        denominador = self.denominador * fracao2.numerador
        
        return Fracao(numerador, denominador)
    
    
 
#declarando as frações   
fracao1 = Fracao(1, 2)
fracao2 = Fracao(3,4)


#realizando as operações
add = fracao1.adicionar(fracao2)
sub = fracao1.subtrair(fracao2)
mult = fracao1.multiplicar(fracao2)
div = fracao1.dividir(fracao2)


print(f'Resultado da adição: {add.numerador}/{add.denominador}')     
print(f'Resultado da subtração: {sub.numerador}/{sub.denominador}')     
print(f'Resultado da multiplicação: {mult.numerador}/{mult.denominador}')     
print(f'Resultado da divisão: {div.numerador}/{div.denominador}')     