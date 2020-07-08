import random
def lista_grande(n):
    lista = []
    while len(lista) < n:
        lista.append(random.randint(1, 999))
    return lista
