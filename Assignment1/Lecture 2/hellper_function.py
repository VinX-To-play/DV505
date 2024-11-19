import math
import matplotlib.pyplot as plt
from three_sum import *
import random
import time

start = 200
stop = 701
step = 50

Savefile = "time.data"

def time_taker(start, stop, step):
    time_data = []
    for i in range(start, stop, step):
        lst = []
        for _ in range(start, i):
            lst.append(random.randint(-10 * i, 10 * i))
        begin_time = time.time()
        sum_3_brut(lst)
        time_data.append((time.time() - begin_time))
        print(time_data[len(time_data) - 1])

    saving_func(time_data)
    return time_data

def saving_func(time_data):
    with open(Savefile, "wt") as data:
        for i in range(len(time_data)):
            data.write(f"{str(time_data[i])} \n")


def read_funk(Savefile):
    with open("time.data", "r") as file:
        data = file.read()
        return data.split()



time_data = read_funk(Savefile)
#time_data = time_taker(start, stop, step)
print(time_data)
saving_func(time_data)


y_axis = range(start, stop, step)
plt.plot(time_data, y_axis)
plt.show()