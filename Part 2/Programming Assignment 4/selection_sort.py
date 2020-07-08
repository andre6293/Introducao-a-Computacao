def ordena(arr):
    if len(arr) <= 1:
        return arr

    start = 0
    while start < len(arr):
        menor = arr[start]
        for i in range(start, len(arr)):
            if arr[i] <= menor:
                menor = arr[i]
                menor_i = i
        arr[start], arr[menor_i] = arr[menor_i], arr[start]
        start += 1
    return arr
