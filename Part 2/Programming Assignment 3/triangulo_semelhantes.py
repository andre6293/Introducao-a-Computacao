class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, Triangulo):
        return (self.a / Triangulo.a == self.b / Triangulo.b and
                self.b / Triangulo.b == self.c / Triangulo.c)
