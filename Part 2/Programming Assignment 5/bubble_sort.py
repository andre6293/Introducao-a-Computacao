def bubble_sort(arr):
    end = len(arr)
    for i in range(end - 1, 0, -1):
        trocou = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
                print(arr)
        if trocou == False:
            return arr
    return arr
