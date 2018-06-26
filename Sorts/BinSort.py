def bin_search(lst, x):
    lower_bound = 0
    upper_bound = len(lst)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2    # Целочисленный тип в Python имеет неограниченную длину
        if x == lst[compared_value]:
            return compared_value
        elif x < lst[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None  # если цикл окончен, то значение не найденно

lst = sorted([int(x) for x in input('Введите массив: ').split()])
x = int(input('Введите искомый элемент: '))
print(bin_search(lst, x))