# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

n = 1
lst = []
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lst.append(n)

lst.reverse()
for i in lst:
    print(i)