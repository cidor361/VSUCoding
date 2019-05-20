from re import search

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from collections import OrderedDict

from matplotlib import mlab
from numpy.linalg import linalg
from scipy.optimize import fsolve


def cleanstring(string):
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.replace("\n", " ")
    string = string.strip(' ')
    return string


def get_from_file(file, data):
    for string in file:
        string = cleanstring(string)
        if string.count(' ') < 2:
            x, y = string.split(' ')
            x = float(x)
            y = float(y)
            data.append([x, y])
        else:
            data = get_from_string(string, data)
        data = list(OrderedDict(data).items())
    return data


def get_from_string(string, data):
    string.strip(' ')
    gaps = string.count(' ') // 2 + 1
    subdata = string.split(' ')
    i = 0
    for i in range(gaps):
        x = subdata[0]
        y = subdata[1]
        x = float(x)
        y = float(y)
        del subdata[0]
        del subdata[0]
        data.append([x, y])
    return data


def cut_list(array):
    i = 0
    x = []
    y = []
    for i in range(len(array)):
        x.append(array[i][0])
        y.append(array[i][1])
    return x, y


def getdata():
    file = open('data.txt', 'r')
    data = []
    data = get_from_file(file, data)
    data.sort()
    x, y = cut_list(data)
    return x, y


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


def points():
    x, y = getdata()
    plt.scatter(x, y)
    plt.show()


def interpolation():
    x, y = getdata()
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [lagranz(x, y, i) for i in xnew]
    plt.plot(x, y, 'o', xnew, ynew)
    plt.grid(True)
    plt.show()


def approximation(d):
    x, y = getdata()
    # d степень полинома
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)  # Модель
    f = sp.poly1d(fp)  # аппроксимирующая функция
    # print('Коэффициент -- a %s  ' % round(fp[0], 4))
    # print('Коэффициент-- b %s  ' % round(fp[1], 4))
    # print('Коэффициент -- c %s  ' % round(fp[2], 4))
    # y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
    # so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
    # print('Average quadratic deviation ' + str(so))
    fx = sp.linspace(x[0], x[-1] + 1, len(x))  # можно установить вместо len(x) большее число для интерполяции\\
    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(fx, f(fx), linewidth=2)
    plt.grid(True)
    plt.show()


# Определение функции
function_f = lambda x: D * np.math.sin(A * x ** B + C)
# Метод золотого сечения
def Golden_Section_Method(x_min, x_max, eps):
    iteration = 1.0
    print((" {0:.8s} || {1:.5s}  || {2:.8s} || {3:.5s}  || {4:.8s}").format("Итерация", "x_min", "f(x_min)", "x_max", "f(x_max)"))
    coefficient = (np.math.sqrt(5) - 1) / 2
    d = x_min + (x_max - x_min) * coefficient
    c = x_max - (x_max - x_min) * coefficient
    sc = function_f(c)
    sd = function_f(d)
    while (x_max - x_min) > eps:
        if (sd < sc):
            x_max = d
            d = c
            c = x_max - (x_max - x_min) * coefficient
            sd = sc
            sc = function_f(c)
        else:
            x_min = c
            c = d
            d = x_min + (x_max - x_min) * coefficient
            sc = sd
            sd = function_f(d)
        iteration += 1
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration - 1, x_min,
                                                                                       function_f(x_min), x_max,
                                                                                       function_f(x_max)))
    # Шаг между точками
    dx = 0.1
    # Создадим список координат по оси X на отрезке [-x_min; x_max], включая концы
    xlist = mlab.frange(x_min, x_max, dx)
    # Вычислим значение функции в заданных точках
    ylist = [function_f(x) for x in xlist]
    # Нарисуем одномерный график
    plt.plot(xlist, ylist, 'o', color='red')
    plt.grid(True)
    # Покажем окно с нарисованным графиком
    # plt.show()


Golden_Section_Method(x_min, x_max, 0.02)
# Шаг между точками
dx = 0.1
# Создадим список координат по оси X на отрезке [-x_min; x_max], включая концы
xlist = mlab.frange(x_min, x_max, dx)
# Вычислим значение функции в заданных точках
ylist = [function_f(x) for x in xlist]
# Нарисуем одномерный график
plt.plot(xlist, ylist, 'o', color='blue')
# Покажем окно с нарисованным графиком
plt.show()