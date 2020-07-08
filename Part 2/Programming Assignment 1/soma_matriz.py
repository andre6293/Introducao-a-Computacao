def soma_matrizes(m1, m2):
    if len(m1) != len(m2):
        return False
    else:
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m1[i][j] += m2[i][j]
    return m1
