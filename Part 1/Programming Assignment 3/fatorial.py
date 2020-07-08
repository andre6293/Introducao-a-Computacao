# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

# Com math

# import math

# n = int(input("Insira o número que deseja o fatorial: "))
# nfac = math.factorial(n)
# print(nfac)

# Sem math
def fatorial(n):
    a = n - 1
    if n == 0:
        print(1)
    else:
        for i in range(n - 1):
            n = n * (a - i)
        return n

print(fatorial(5))
