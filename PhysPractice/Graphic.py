import re
import matplotlib.pyplot as plt
import numpy as np

reg = re.compile('[^0-9.\s ]')

with open("data.txt") as file:
    array = [row.strip() for row in file]

i = 0
for i in range(len(array)):
    array[i] = reg.sub('', array[i]).split(' ')
    if len(array[i]) > 2:
        num_of_path = len(array) // 2
        subarray = array[i]
        del array[i]
        k = 0
        for k in range(num_of_path):
            array.append([subarray[k * 2], subarray[k * 2 - 1]])

xt = []
yt = []
i = 0
for i in range(len(array)):
    x, y = array[i]
    x = float(x)
    y = float(y)
    xt.append(x)
    yt.append(y)
    plt.scatter(x, y)
plt.plot(xt, yt)
# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
# fig, ax = plt.subplots()
# ax.errorbar(xt, yt, xerr=0.2, yerr=0.4)
plt.show()
