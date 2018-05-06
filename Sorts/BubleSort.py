def BubbleSort(array):
    for j in range(len(array) - 1):

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    print(array)

array = [7, 9, 5, 4]

BubbleSort(array)