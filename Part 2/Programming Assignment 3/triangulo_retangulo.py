class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5 == self.c
