from collections import OrderedDict
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from matplotlib import mlab


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


def Golden_Select(x_min, x_max):
    #Определение переменных
    A = 1.5; B = 1; C = 3; D = 1.5;
    # x_min = 2.2
    # x_max = 4.4
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
    plt.plot(xlist, ylist, color='blue')
    # Покажем окно с нарисованным графиком
    plt.show()


# Golden_Select(0, 10)


def fibonachi(n, Xl, Xr, par):
    # n = int(input("Кол-во экспериментов: "))
    # Xl = float(input("Левый предел: "))
    # Xr = float(input("Правый предел: "))
    # par = input("max или min:")
    n = int(n)
    Xl = float(Xl)
    Xr = float(Xr)

    def fibonacci(fun, Xl, Xr, n, par="max"):
        def num_Fib(n):
            terms = [0, 1]
            i = 2
            while i <= n:
                terms.append(terms[i - 1] + terms[i - 2])
                i += 1
            return terms[n]

        EPS = 0.001
        a = list([0, Xl])
        b = list([0, Xr])
        lam = lambda n: (num_Fib(n - 2) / num_Fib(n)) * (a[k] - b[k]) + a[k]
        mu = lambda n: (num_Fib(n - 1) / num_Fib(n)) * (a[k] - b[k]) + a[k]
        f_lam = lambda k: fun(lam(k))
        f_mu = lambda k: fun(mu(k))
        k = 1

        if par == "min":
            for k in range(1, n):
                if f_lam(k) > f_mu(k):
                    a.append(lam(k))
                    b.append(b[k])
                    lam_k_plus = mu(k)
                    mu_k_plus = (a[k + 1]) + (num_Fib(n - k - 1) / num_Fib(n - k)) * ((b[k + 1]) - (a[k + 1]))
                    if k == (n - 2):
                        # step 5
                        lam_n = lam(n - 1)
                        mu_n = lam(n) + EPS
                        if f_lam(n) == f_mu(n):
                            a_n = lam(n)
                            b_n = b[n - 1]
                        elif f_lam(n) < f_mu(n):
                            a_n = a[n - 1]
                            b_n = mu(n)
                        else:
                            print("Непредвиденый исход. 1")
                    else:
                        k += 1
                        # print("Part 2, Step 3:\n\tf_mu[k] = {}\n\tf_lam[k] = {}".format(f_mu(k), f_lam(k)))
                else:
                    a.append(a[k])
                    b.append(mu(k))
                    mu_k_plus = lam(k)
                    lam_k_plus = a[k + 1] + (num_Fib(n - k - 2) / num_Fib(n - k)) * (b[k + 1] - a[k + 1])
                    if k == (n - 2):
                        # step 5
                        lam_n = lam(n - 1)
                        mu_n = lam(n) + EPS
                        if f_lam(n) == f_mu(n):
                            a_n = lam(n)
                            b_n = b[n - 1]
                        elif f_lam(n) < f_mu(n):
                            a_n = a[n - 1]
                            b_n = mu(n)
                        else:
                            print("Непредвиденый исход. 2")
                    else:
                        k += 1
                        # print("Part 2, Step 3:\n\tf_mu[k] = {}\n\tf_lam[k] = {}".format(f_mu(k), f_lam(k)))
            return a[k], f_mu(k)
        else:
            for k in range(1, n):
                if f_lam(k) < f_mu(k):
                    a.append(lam(k))
                    b.append(b[k])
                    lam_k_plus = mu(k)
                    mu_k_plus = (a[k + 1]) + (num_Fib(n - k - 1) / num_Fib(n - k)) * ((b[k + 1]) - (a[k + 1]))
                    if k == (n - 2):
                        # step 5
                        lam_n = lam(n - 1)
                        mu_n = lam(n) + EPS
                        if f_lam(n) == f_mu(n):
                            a_n = lam(n)
                            b_n = b[n - 1]
                        elif f_lam(n) < f_mu(n):
                            a_n = a[n - 1]
                            b_n = mu(n)
                        else:
                            print("Code: 1")
                    else:
                        k += 1
                        # print("Part 2, Step 3:\n\tf_mu[k] = {}\n\tf_lam[k] = {}".format(f_mu(k), f_lam(k)))
                else:
                    a.append(a[k])
                    b.append(mu(k))
                    mu_k_plus = lam(k)
                    lam_k_plus = a[k + 1] + (num_Fib(n - k - 2) / num_Fib(n - k)) * (b[k + 1] - a[k + 1])
                    if k == (n - 2):
                        # step 5
                        lam_n = lam(n - 1)
                        mu_n = lam(n) + EPS
                        if f_lam(n) == f_mu(n):
                            a_n = lam(n)
                            b_n = b[n - 1]
                        elif f_lam(n) < f_mu(n):
                            a_n = a[n - 1]
                            b_n = mu(n)
                        else:
                            print("Code: 2")
                    else:
                        k += 1
                        # print("Part 2, Step 3:\n\tf_mu[k] = {}\n\tf_lam[k] = {}".format(f_mu(k), f_lam(k)))
            return a[k], f_mu(k)

    # --------------------------------------------------------------TEST MAX-----------------------------------------------
    print("----------------------------------------TEST MAX----------------------------------------")
    first_fun_max = lambda x: (x**Xl)*math.sin(Xr * x)
    second_fun_max = lambda x: ((math.e ** (Xl * x)) * (math.cos(Xr * x)))
    third_fun_max = lambda x: (1 - math.fabs(Xl) * (x ** 2)) * math.atan(1 + math.fabs(Xr) * (x ** 2))

    X, F_X = fibonacci(first_fun_max, Xl, Xr, n, "max")
    print("MAX\n\tf(x) = x^a * sin(bx)\n\tX = {}, F(X) = {}".format(X, F_X))

    X, F_X = fibonacci(second_fun_max, Xl, Xr, n, "max")
    print("MAX\n\tf(x) = e^ax * cos(bx)\n\tX = {}, F(X) = {}".format(X, F_X))

    X, F_X = fibonacci(third_fun_max, Xl, Xr, n, "max")
    print("MAX\n\tf(x) = (1 - |a|*x^2) * arctg(1 - |b|*x^2)\n\tX = {}, F(X) = {}".format(X, F_X))
    # --------------------------------------------------------------TEST MIN-----------------------------------------------
    print("----------------------------------------TEST MIN----------------------------------------")
    first_fun_min = lambda x: (x**2) + (Xl * math.e**Xr * x)
    second_fun_min = lambda x: (x**4) + math.atan(Xr * x)
    third_fun_min = lambda x: Xr*x + (math.e**(abs(x - Xl)))

    X, F_X = fibonacci(first_fun_min, Xl, Xr, n, "min")
    print("MIN\n\tf(x) = x**2 + (a * e**b * x)\n\tX = {}, F(X) = {}".format(X, F_X))

    X, F_X = fibonacci(second_fun_min, Xl, Xr, n, "min")
    print("MIN\n\tf(x) = x**4 + arctg(b * x)\n\tX = {}, F(X) = {}".format(X, F_X))

    # X, F_X = fibonacci(third_fun_min, Xl, Xr, n, "min")
    # print("MIN\n\tf(x) = b * x + e**(abs(x - a))\n\tX = {}, F(X) = {}".format(X, F_X))


# fibonachi(10, 0, 100, 'max')


def dichotom(EPS, Xl, Xr, par):
    # EPS = float(input("Погрешность: "))
    # Xl = float(input("Левый предел: "))
    # Xr = float(input("Правый предел: "))
    # par = input("max или min:")
    EPS = float(EPS)
    Xl = float(Xl)
    Xr = float(Xr)
    def dichotomy(fun, X_left, X_right, EPS, par="max"):
        a = float(X_left)
        b = float(X_right)
        n = 0  # Проведенное кол-во итераций
        c = 0
        while (abs(b) - abs(a)) > EPS:
            n += 1
            c = (b + a) / 2
            if par.lower() == "max":
                if fun(c-EPS) > fun(c+EPS):
                    b = c
                else:
                    a = c
            else:
                if fun(c-EPS) < fun(c+EPS):
                    b = c
                else:
                    a = c
            # print("n: {}, a: {}, b: {}".format(n, a, b))
        return c, fun(c)


    # --------------------------------------------------------------TEST MAX-----------------------------------------------
    print("----------------------------------------TEST MAX----------------------------------------")
    first_fun_max = lambda x: (x**Xl)*math.sin(Xr * x)
    second_fun_max = lambda x: ((math.e ** (Xl * x)) * (math.cos(Xr * x)))
    third_fun_max = lambda x: (1 - math.fabs(Xl) * (x ** 2)) * math.atan(1 + math.fabs(Xr) * (x ** 2))

    x_nm, y_nm = dichotomy(first_fun_max, Xl, Xr, EPS)
    print("MAX\n\tf(x) = x^a * sin(bx)\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))

    x_nm, y_nm = dichotomy(second_fun_max, Xl, Xr, EPS)
    print("MAX\n\tf(x) = e^ax * cos(bx)\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))

    x_nm, y_nm = dichotomy(third_fun_max, Xl, Xr, EPS)
    print("MAX\n\tf(x) = (1 - |a|*x^2) * arctg(1 - |b|*x^2)\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))


    # --------------------------------------------------------------TEST MIN-----------------------------------------------
    print("----------------------------------------TEST MIN----------------------------------------")
    first_fun_min = lambda x: (x**2) + (Xl * (math.e**Xr) * x)
    second_fun_min = lambda x: (x**4) + math.atan(Xr * x)
    third_fun_min = lambda x: Xr*x + (math.e**(abs(x - Xl)))

    x_nm, y_nm = dichotomy(first_fun_min, Xl, Xr, EPS, "min")
    print("MIN\n\tf(x) = x**2 + (a * e**b * x)\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))

    x_nm, y_nm = dichotomy(second_fun_min, Xl, Xr, EPS, "min")
    print("MIN\n\tf(x) = x**4 + arctg(b * x)\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))

    # x_nm, y_nm = dichotomy(third_fun_min, Xl, Xr, EPS, "min")
    # print("MIN\n\tf(x) = b * x + e**(abs(x - a))\n\tx_nm: {}, y_nm: {}, EPS: {}".format(x_nm, y_nm, EPS))


# dichotom(0.1, 0, 10, 'max')
