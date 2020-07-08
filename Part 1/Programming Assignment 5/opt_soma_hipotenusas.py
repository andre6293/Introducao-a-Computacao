# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def eHipotenusa(n):
    for i in range(1, n):
        for j in range(1, n):
            if i ** 2 + j ** 2 == n ** 2:
                return True
    return False

def soma_hipotenusas(n):
    hipotenusas = []
    for i in range(1, n + 1):
        if eHipotenusa(i):
            hipotenusas.append(i)
    return sum(hipotenusas)

print(soma_hipotenusas(25))