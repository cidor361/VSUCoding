import re
import matplotlib.pyplot as plt
import numpy as np

reg = re.compile('[^0-9.\s]')

f = open('data.txt', 'r')
# data = f.read()
# data = reg.sub('', data)
i = 0
data = []
for line in f:
    if line.count(' ') < 3:
        data.append(reg.sub('', line))
    else:
        spaces = line.count(' ')
        cut = spaces // 2

# print(data)
# with open("data.txt") as file:
#     array = [row.strip() for row in file]
# print(array)
# for i in range(len(array)):
#     array[i] = array[i].replace("(", "")
#     array[i] = array[i].replace(")", "")
#     print(array[i])

# i = 0
# for i in range(len(array)):
#     # array[i] = reg.sub('', array[i]).split(' ')
#     if array[i].count(' ') > 2:
#         num_of_path = array[i].count(' ') // 2
#         subarray = array[i]
#         print(subarray)
#         del array[i]
#         k = 0
#         for k in range(num_of_path):
#             array.append([subarray[k * 2], subarray[k * 2 - 1]])
# print(array)
# coordinates = []
# i = 0
# for i in range(len(array)):
#     x, y = array[i]
#     x = float(x)
#     y = float(y)
#     coordinate = [x, y]
#     coordinates.append(coordinate)
    # plt.scatter(coordinates[i])
# print(coordinates)
# plt.plot(xt, yt)

# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
# fig, ax = plt.subplots()
# ax.errorbar(xt, yt, xerr=0.2, yerr=0.4)

# plt.show()
