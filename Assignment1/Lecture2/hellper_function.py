import math
import matplotlib.pyplot as plt
from three_sum import *
import random
import time

start = 300
stop = 701
step = 50
prsison = 5

Savefile = "time.data"

def time_taker(start, stop, step):
    time_data = []
    for i in range(start, stop, step):
        lst = []
        temp_time = 0
        for _ in range(prsison):
            for _ in range(i):
                lst.append(random.randint(-10 * i, 10 * i))
            begin_time = time.time()
            sum_3_brut(lst)
            test_time = ((time.time() - begin_time))
            temp_time += test_time
            print(test_time, 'run')
            test_time = 0
            lst = []
        time_data.append(temp_time / prsison)
        print(time_data[len(time_data) - 1], 'averig')
        

    saving_func(time_data)
    return time_data

def saving_func(time_data):
    with open(Savefile, "wt") as data:
        for i in range(len(time_data)):
            data.write(f"{str(time_data[i])} \n")

def lin_reg(x,y):
    n = len(x)
    Sx = sum(x)
    Sy = sum(y)
    Sxx = sum([(e ** 2) for e in x])
    Sxy = 0 
    for i in range(n):
        Sxy += x[i] * y[i]
    m = ((Sxx * Sy) - (Sx * Sxy)) / ((n * Sxx) - (Sx * Sx))
    k = ((n * Sxy) - (Sx * Sy)) / ((n * Sxx) - (Sx * Sx))
    return m, k


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
    plt.plot(x_axis, time_data, '+')
    plt.show()


def log_graph(start, stop, step, time_data):
    x_axis = [*range(start, stop, step)]
    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc in log")
    plt.ylabel("time in log")
    logX = [math.log(x) for x in x_axis]
    logY = [math.log(y) for y in time_data]
    m , k = lin_reg(logX, logY)
    lineY = [(m + x * k) for x in logX]
    plt.title(f'k = {k}')
    plt.plot(logX, logY, '+')
    plt.plot(logX, lineY, '-')
    plt.show()



#time_data = read_funk(Savefile)
time_data = time_taker(start, stop, step)
print(time_data)
saving_func(time_data)
lin_graph(start, stop, step,time_data)
log_graph(start, stop, step,time_data)
