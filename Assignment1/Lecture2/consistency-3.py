import matplotlib.pyplot as plt
import math
from lin_reg import *


start = 100
stop = 701
step = 25

def read_funk(Savefile):
    with open(Savefile, "r") as file:
        time_data = []
        data = file.read()
        for i in data.split():
            time_data.append(float(i))
        return time_data

time_data = read_funk('Assignment1/Lecture2/data/time_0.data')
time1_data = read_funk('Assignment1/Lecture2/data/time_1.data')
time2_data = read_funk('Assignment1/Lecture2/data/time_2.data')


x_axis = [*range(start, stop, step)]
plt.xlabel(f"iterration from {start} to {stop} in {step} distanc")
plt.plot(x_axis, time_data,'+', color='b', label='1.' )
plt.plot(x_axis, time1_data, '+',color='g', label='2.')
plt.plot(x_axis, time2_data, '+',color='r', label='3.')

plt.legend()
plt.show()

plt.xlabel(f"iterration from {start} to {stop} in {step} distanc in log")
plt.ylabel("time in log")
logX = [math.log(x) for x in x_axis]
logY = [math.log(y) for y in time_data]
logY1 = [math.log(y) for y in time1_data]
logY2 = [math.log(y) for y in time2_data]

plt.plot(logX, logY, '+',color='b', label='1.')
plt.plot(logX, logY1, '+',color='g', label='2.')
plt.plot(logX, logY2, '+',color='r', label='3.')
plt.legend()
plt.show()