# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def ePrimo(n):
    if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
                return False
       else:
           return True
    return False

def n_primos(n):
    primos = 0
    for i in range(2, n + 1):
        if ePrimo(i):
            primos += 1
    return primos
