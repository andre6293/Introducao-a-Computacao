# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def mediaDeQuatroNotas():
    notas = []
    notas.append(int(input("Digite a primeira nota: ")))
    notas.append(int(input("Digite a segunda nota: ")))
    notas.append(int(input("Digite a terceira nota: ")))
    notas.append(int(input("Digite a quarta nota: ")))
    return "A média aritmética é " + str(sum(notas)/len(notas))

print(mediaDeQuatroNotas())