import numpy
import matplotlib.pyplot as plt
from three_sum import *
import random
import time


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

time_data = time_taker(200,701,50)
print(time_data)


