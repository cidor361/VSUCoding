import re
import matplotlib.pyplot as plt
import numpy as np

# plt.scatter(x, y)

# with open("data.txt") as file:
#     array = [row.strip() for row in file]
# for i in range(len(array)):
#     array[i] = array[i].replace("(", "")
#     array[i] = array[i].replace(")", "")

# i = 0
# for i in range(len(array)):
#     # array[i] = reg.sub('', array[i]).split(' ')
#     if array[i].count(' ') > 2:
#         num_of_path = array[i].count(' ') // 2
#         subarray = array[i]
#         del array[i]
#         k = 0
#         for k in range(num_of_path):
#             array.append([subarray[k * 2], subarray[k * 2 - 1]])
# coordinates = []
# i = 0
# for i in range(len(array)):
#     x, y = array[i]
#     x = float(x)
#     y = float(y)
#     coordinate = [x, y]
#     coordinates.append(coordinate)
# plt.scatter(coordinates[i])
# plt.plot(xt, yt)

# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
# fig, ax = plt.subplots()
# ax.errorbar(xt, yt, xerr=0.2, yerr=0.4)

# plt.show()
from scipy.interpolate import interp1d


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
    string = string.strip(' ')
    return string


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
    f = interp1d(x, y)


getdata()
