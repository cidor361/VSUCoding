def Pyramid():
    i = 0
    OutString = ''

    while True:
        try:
            PyramidHeit = int(input("Введите число: "))
            if 0 < PyramidHeit < 24:
                break
            else:
                raise ValueError
        except ValueError:
            print("Вы ввели не число или оно не входит в диапазон. Попробуйте снова: ")

    while i != PyramidHeit:
        i += 1

        if i > 1:
            OutString = ' ' * (PyramidHeit - i)
            OutString += '#' * i
            print(OutString)

        elif i == 1:
            OutString = ' ' * (PyramidHeit - i)
            OutString += str(PyramidHeit)
            print(OutString)



Pyramid()
