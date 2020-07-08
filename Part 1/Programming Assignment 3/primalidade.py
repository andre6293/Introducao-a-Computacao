# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

n = int(input("Digite um número inteiro: "))
divisores = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisores += 1

if divisores <= 2:
    print("primo")
else:
    print("não primo")
