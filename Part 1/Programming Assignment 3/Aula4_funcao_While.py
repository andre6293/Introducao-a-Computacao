# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

lst = []
# for i in range(2, 14):
#     lst.append(2 ** i)

# for i in range(len(lst)):
#     print(lst[i])

# i = 0
# while i <= 10:
#     lst.append(2 ** i)
#     i += 1

# print(lst)

produto = 1
valor = 1
while valor != 0:
    valor = (int(input("Digite valor a ser somado: ")))
    if valor == 0:
        pass
    else:
        produto = produto * valor
print("O produto dos valores digitados é", str(produto))
