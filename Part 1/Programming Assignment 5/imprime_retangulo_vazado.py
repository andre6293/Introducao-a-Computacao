# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
print("#" * largura)
altura -= 1

while altura > 1:
    print("#" + (" " * (largura - 2) + "#"))
    altura -= 1

print("#" * largura, end="")