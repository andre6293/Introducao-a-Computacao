def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr
