def SelectSort(array):
    for i in range(0, len(array) - 1):
        MinNum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[MinNum]:
                MinNum = j
        array[i], array[MinNum] = array[MinNum], array[i]

array = [7, 9, 5, 4]

SelectSort(array)

print(array)