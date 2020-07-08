# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def areaQuadrado():
    lado = int(input("Digite o tamanho do lado do quadrado: "))
    perimetro = lado * 4
    area = lado * lado
    return "perímetro: " + str(perimetro) + " - área: " + str(area)


print(areaQuadrado())