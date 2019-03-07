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
            array.append([subarray[k*2], subarray[k*2-1]])

if len(array) == 1:
    array = array[0]
    i = 0
    for i in range(len(array) // 2):
        x = array[i * 2]
        y = array[i * 2 - 1]
        x = float(x)
        y = float(y)
        plt.scatter(x, y)
else:
    i = 1
    for i in range(len(array)):
        x, y = array[i]
        x = float(x)
        y = float(y)
        plt.scatter(x, y)
plt.show()
