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


def approximation():
    x, y = getdata()
    d = 2  # степень полинома
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)  # Модель
    f = sp.poly1d(fp)  # аппроксимирующая функция
    print('Коэффициент -- a %s  ' % round(fp[0], 4))
    print('Коэффициент-- b %s  ' % round(fp[1], 4))
    print('Коэффициент -- c %s  ' % round(fp[2], 4))
    y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
    so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
    print('Average quadratic deviation ' + str(so))
    fx = sp.linspace(x[0], x[-1] + 1, len(x))  # можно установить вместо len(x) большее число для интерполяции\\
    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(fx, f(fx), linewidth=2)
    plt.grid(True)
    plt.show()


def aprox():
    x, y = getdata()
    # настраиваем детали отрисовки графиков
    plt.figure(figsize=(8, 6))
    plt.title("Installations")
    plt.xlabel("Days")
    plt.ylabel("Installations")
    # plt.xticks([...], [...]) # можно назначить свои тики
    plt.autoscale(tight=True)

    # рисуем исходные точки
    plt.scatter(x, y)

    legend = []
    # аргументы для построения графиков моделей: исходный интервал + 60 дней
    fx = sp.linspace(x[0], x[-1] + 60, 1000)
    for d in range(1, 6):
        # получаем параметры модели для полинома степени d
        fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)
        # print("Параметры модели: %s" % fp1)
        # функция-полином, если её напечатать, то увидите математическое выражение
        f = sp.poly1d(fp)
        # print(f)
        # рисуем график модельной функции
        plt.plot(fx, f(fx), linewidth=2)
        legend.append("d=%i" % f.order)
        f2 = f - 1000  # из полинома можно вычитать
        t = fsolve(f2, x[-1])  # ищем решение уравнения f2(x)=0, отплясывая от точки x[-1]
        print("Полином %d-й степени:" % f.order)
        print("- Мы достигнем 1000 установок через %d дней" % (t[0] - x[-1]))
        print("- Через 60 дней у нас будет %d установок" % f(x[-1] + 60))
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.savefig('data.png', dpi=50)
    plt.show()


approximation()