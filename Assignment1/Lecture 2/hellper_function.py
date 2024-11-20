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
        for _ in range(i):
            lst.append(random.randint(-100, 100))
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
        time_data = []
        data = file.read()
        for i in data.split():
            time_data.append(float(i))
        return time_data

def lin_graph(start, stop, step, time_data):
    x_axis = [*range(start, stop, step)]
    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc")
    plt.ylabel("time")
    plt.plot(x_axis, time_data)
    plt.show()


def log_graph(start, stop, step, time_data):
    x_axis = [*range(start, stop, step)]
    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc in log")
    plt.ylabel("time in log")
    logX = [math.log(x) for x in x_axis]
    logY = [math.log(y) for y in time_data]
    for i in range(len(time_data)):
        print(logY[i], time_data[i])
    plt.plot(logX, logY)
    plt.show()



#time_data = read_funk(Savefile)
time_data = time_taker(start, stop, step)
print(time_data)
saving_func(time_data)
lin_graph(start, stop, step,time_data)
log_graph(start, stop, step,time_data)
