import matplotlib.pyplot as plt
import numpy as np


def cleanstring(string):
    string = string.replace("!", "")
    string = string.replace("@", "")
    string = string.replace("#", "")
    string = string.replace("$", "")
    string = string.replace("%", "")
    string = string.replace("^", "")
    string = string.replace("&", "")
    string = string.replace("*", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.replace("+", "")
    string = string.replace("=", "")
    string = string.replace("?", "")
    string = string.replace("\'", "")
    string = string.replace("\"", "")
    string = string.replace("{", "")
    string = string.replace("}", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("<", "")
    string = string.replace(">", "")
    string = string.replace("~", "")
    string = string.replace("`", "")
    string = string.replace(":", "")
    string = string.replace(";", "")
    string = string.replace("|", "")
    string = string.replace("\\", "")
    string = string.replace("/", "")
    string = string.replace(",", "")
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
    print(x, y)
    xx = np.array(x, dtype=float)
    yy = np.array(y, dtype=float)
    print(x, y)
    return xx, yy


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


x, y = getdata()
xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()
