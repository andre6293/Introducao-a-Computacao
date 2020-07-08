# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

n = input("Digite um número inteiro: ")
lgth = len(n)
adjacente = False

if lgth < 2:
    pass
else:    
    for i in range(lgth):
        if i == 0:
            if (n[i] == n[i + 1]):
                adjacente = True
                break
            else:
                adjacente = False
        elif i == (lgth - 1):
            if (n[i] == n[i - 1]):
                adjacente = True
                break
            else:
                adjacente = False
                break
        else:
            if (n[i] == n[i + 1]) or (n[i] == n[i - 1]):
                adjacente = True
                break
            else:
                adjacente = False

if adjacente:
    print("sim")
else:
    print("não")
