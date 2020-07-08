# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def fatura():
    cliente = input("Digite o nome do cliente: ")
    diaVencimento = input("Digite o dia de vencimento: ")
    mesVencimento = input("Digite o mês de vencimento: ")
    valor = input("Digite o valor da fatura: ")
    return "Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(cliente, diaVencimento, mesVencimento, valor)

print(fatura())