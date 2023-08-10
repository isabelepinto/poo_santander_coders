# módulo para formas geométricas que implemente classes para Retângulo, Quadrado, Triangulo, Circulo

class Retangulo:
    def __init__(self, lado: float, altura:float) -> None:
        self.lado = lado
        self.altura = altura
    
    def area(self):
        return self.lado * self.altura
    

class Quadrado:
    def __init__(self, lado: float, altura:float) -> None:
        self.lado = lado
        self.altura = altura
    
    def area(self):
        if self.lado == self.altura:
            return self.lado * self.altura
        else:
            return 'Essas informações não correspondem a um quadrado'
    

class Triangulo:
    def __init__(self, base: float, altura:float) -> None:
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura / 2
    

class Circulo:
    def __init__(self, raiz) -> None:
        self.raiz = raiz
    
    def area(self):
        PI = 3.14
        return PI * (self.raiz ** 2)
    
