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

def maiorPrimo(n):
    for i in range(n, 2, -1):
        if ePrimo(i):
            return i
    return 0
