def InsertSort(array):
    for i in range(1, len(array)):
        NewElement = array[i]
        j = i - 1
        while j >= 0 and array[j] > NewElement:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = NewElement
    print(array)

array = [7, 9, 5, 4]

InsertSort(array)