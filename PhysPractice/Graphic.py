from re import search

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from collections import OrderedDict

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


def f(x):
    return 10


def MPD(f, a, b):
    eps = 10e-5
    while abs(b - a) >= eps:
        c = (b + a) / 2.0
        if f == 0:
            break
        elif f(a) < 0:
            b = c
        else:
            a = c
        return c


# print(MPD(f, 1, 1000))


def


#
#
# def halfIntervalMethod(f, a, b):
#     aVal = f(a)
#     bVal = f(b)
#     if aVal > 0 and bVal < 0:
#         return search(f, b, a)
#     elif aVal < 0 and bVal > 0:
#         return search(f, a, b)
#     else:
#         print("У аргументов не разные знаки")
#         return 0
#
#
# halfIntervalMethod(f, 1, 2)


# def f(x, a, b):
#     return x ** 2
#     # return x**a*sin(b*x)
#
#
# def max_of_func_1(f, a, b, eps=1e-5):
#     while abs(b - a) > eps:
#         x = (a + b) / 2.0
#         fx = f(x, a, b)
#         fa = f(a, a, b)
#         if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
#             a = x
#         else:
#             b = x
#     return x
#
#
# a = 0
# b = 2
# x = max_of_func_1(f, 0, 1)
# print(x)
# print(f(x, a, b))
# plt.plot(x, f(x, a, b), 'o')
# plt.grid(True)
# plt.show()
