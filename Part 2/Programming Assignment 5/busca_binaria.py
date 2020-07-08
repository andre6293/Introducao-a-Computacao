def busca(arr, item):
    primeiro = 0
    ultimo = len(arr) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if arr[meio] == item:
            return meio
        else:
            if item < arr[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False
