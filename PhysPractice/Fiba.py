# Подключение библиотек
import math
import pylab
import matplotlib.pyplot as plt
from matplotlib import mlab

# Определение переменных
x_min = 2.2
x_max = 4.4
number_of_iterations = 10

# Определение функции
function_fun = []
function_fun.append(lambda x: (x ** x_min) * math.sin(x_max * x))
function_fun.append(lambda x: ((math.e ** (x_min * x)) * (math.cos(x_max * x))))
function_fun.append(lambda x: (1 - math.fabs(x_min) * (x ** 2)) * math.atan(1 + math.fabs(x_max) * (x ** 2)))

# number_of_iterations = int(input(" Введите количество итераций: "))


# Число Фибоначчи
def Fibonacci(n):
    return int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))


print((" {0:.8s} || {1:.5s}  || {2:.8s} || {3:.5s}  || {4:.8s}").format("Итерация", "x_min", "f(x_min)", "x_max",
                                                                        "f(x_max)"))


# Метод Фибоначчи
def Fibonacci_Method(x_min, x_max, iteration=0):
    if (iteration == number_of_iterations): return
    x_lhs = x_min + (((x_max - x_min) * Fibonacci(number_of_iterations - iteration - 1)) / Fibonacci(
        number_of_iterations - iteration + 1))
    x_rhs = x_min + (((x_max - x_min) * Fibonacci(number_of_iterations - iteration)) / Fibonacci(
        number_of_iterations - iteration + 1))
    if (function_f(x_lhs) < function_f(x_rhs)):
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration + 1, x_lhs,
                                                                                       function_f(x_min), x_rhs,
                                                                                       function_f(x_max)))
        Fibonacci_Method(x_lhs, x_max, iteration + 1)
    else:
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration + 1, x_lhs,
                                                                                       function_f(x_min), x_rhs,
                                                                                       function_f(x_max)))
        Fibonacci_Method(x_min, x_rhs, iteration + 1)


i = 0
for i in range(3):
    function_f = function_fun[i]
    Fibonacci_Method(x_min, x_max)
    i += 1

# Шаг между точками
increment = 0.01

# Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(x_min, x_max, increment)

# Вычислим значение функции в заданных точках
ylist = [function_f(x) for x in xlist]

# Нарисуем одномерный график
pylab.plot(xlist, ylist)
plt.grid(True)

# Покажем окно с нарисованным графиком
pylab.show()
