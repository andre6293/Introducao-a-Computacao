def soma_lista(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        return arr[0] + soma_lista(arr[1:])

