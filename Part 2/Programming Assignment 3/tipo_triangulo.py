class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif ((self.a == self.b and self.b != self.c) or
              (self.b == self.c and self.b != self.a) or
              (self.a == self.c and self.a != self.b)):
            return 'isósceles'
        else:
            return 'escaleno'
