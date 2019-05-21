# -*- coding: utf-8 -*-

# Подключение библиотек
import math
import pylab
import matplotlib.pyplot as plt
from matplotlib import mlab

xmin = 2.2
xmax = 4.4

# Определение переменных
function_fun = []
function_fun.append(lambda x: (x**xmin)*math.sin(xmax * x))
function_fun.append(lambda x: ((math.e ** (xmin * x)) * (math.cos(xmax * x))))
function_fun.append(lambda x: (1 - math.fabs(xmin) * (x ** 2)) * math.atan(1 + math.fabs(xmax) * (x ** 2)))


# Метод поперечного сечения
def Half_Division_Method(xmin, xmax, eps):

    while (abs((xmin - xmax)) > eps):
        middle_point = (xmin + xmax) / 2
        if (f(middle_point + 0.01) > f(middle_point - 0.01)):
            print("{0:.4f} || {1:.4f} || Правый".format(middle_point, f(middle_point)))
            xmin = middle_point

        else:
            print("{0:.4f} || {1:.4f} || Левый".format(middle_point, f(middle_point)))
            xmax = middle_point
    print("Интервал нахождения максимума функции: [{0:.4f} ; {1:.4f}]".format(xmin, xmax))


i = 0
for i in range(3):
    f = function_fun[i]
    Half_Division_Method(xmin, xmax, 0.01)
    i += 1

# Шаг между точками
dx = 0.1

# Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [f(x) for x in xlist]

# Нарисуем одномерный график
pylab.plot(xlist, ylist)
plt.grid(True)

# Покажем окно с нарисованным графиком
# pylab.show()
