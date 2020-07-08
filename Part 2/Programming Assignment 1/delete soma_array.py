def soma_array(ar1, ar2):
    if len(ar1) >= len(ar2):
        for i in range(len(ar1)):
            ar1[i] += ar2[i]
        return (print(ar1))
    else:
        for i in range(len(ar2)):
            ar1[i] += ar2[i]
        return (print(ar1))



x = [1, 2, 3]
y = [4]

soma_array(x, y)