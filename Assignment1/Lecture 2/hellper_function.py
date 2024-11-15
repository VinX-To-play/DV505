import pickle
import numpy
import matplotlib.pyplot as plt
from three_sum import *
import random
import time

start = 200
stop = 701
step = 50

def time_taker(start, stop, step):
    time_data = []
    for i in range(start, stop, step):
        lst = []
        for _ in range(start, i):
            lst.append(random.randint(-10 * i, 10 * i))
        begin_time = time.time()
        sum_3_brut(lst)
        time_data.append((time.time() - begin_time))
    return time_data

time_data = time_taker(start, stop, step)
print(time_data)

with open('save.pkl', 'wb') as save:
    pickle.dump(time_data, save, -1)

plt.plot((range(start,stop + 1, step)), time_data)
