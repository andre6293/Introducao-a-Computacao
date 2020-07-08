# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def éPrimo(k):
    divisores = 0

    for i in range(1, k + 1):
        if k % i == 0:
            divisores += 1

    if divisores <= 2:
        return "primo"
    else:
        return"n primo"


def maior_primo(n):
    if éPrimo(n) == "primo":
        return n
    else:
        while True:
            if éPrimo(n) == "primo":
                break
            else:
                n -= 1
        return n
