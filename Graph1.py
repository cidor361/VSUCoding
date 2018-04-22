def func(x):
    return(x**2)

def drawFunc(dx, minX, maxX):
    lengthX = int((maxX - minX) / dx + 1)
    x = []
    y = []
    minY = 10**5
    maxY = -10**5
    str = ''

    for i in range(lengthX):
        x.append(minX + i * dx)
        y.append(func(x[i]))
        if y[i] > maxY: maxY = y[i]
        if y[i] < minY: minY = y[i]
        # print(x[i])
        lengthY = int((maxY - minY) / dx)

    list.reverse(x)
    list.reverse(y)



    for j in range(lengthY):
        for i in range(lengthX):
            if y[lengthX - i - 1] == lengthY - j:
                str += '*'
            else:
                str += ' '
        print(str)
        str = ''


drawFunc(0.1, -10, 10)