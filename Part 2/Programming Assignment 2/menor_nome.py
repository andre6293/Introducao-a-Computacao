def menor_nome(arr):
    '''Devolve o nome mais curto dentro de uma lista'''
    menor = arr[0].strip()
    for i in range(1, len(arr)):
        if len(arr[i].strip()) < len(menor):
            menor = arr[i].strip()
    return str(menor).capitalize()
