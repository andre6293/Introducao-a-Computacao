def busca(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return False
