# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def printDezena1(): # approach "pythonico"
    num = input("Entre o número que deseja o dígito da dezena: ")
    return num[-2]

def printDezena2():
    num = int(input("Entre o número que deseja o dígito da dezena: "))
    return (num // 10) % 10
