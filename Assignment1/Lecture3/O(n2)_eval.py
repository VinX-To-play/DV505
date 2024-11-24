import time
import sort_algorithms as sa
import random
import matplotlib.pyplot as plt
import math
from lin_reg import *

# n^2 test values
start = 700
stop = 6001
step = 350
prsison = 5

# eval O(n^2) 
def test(func):
    time_data = []
    for i in range(start, stop, step):
        lst = []
        temp_time = 0
        for _ in range(prsison):
            for _ in range(i):
                lst.append(random.randint(-10 * i, 10 * i))
            begin_time = time.time()
            func(lst)
            test_time = ((time.time() - begin_time))
            temp_time += test_time
            print(test_time, 'run')
            test_time = 0
            lst = []
        time_data.append(temp_time / prsison)
        print(time_data[len(time_data) - 1], 'averig')
    return time_data


def vis_n_2():
    selection_time = test(sa.selection_sort)
    insertion_time = test(sa.insertion_sort)
    bubbls_time = test(sa.bubble_sort)
    
    x_axis = [*range(start, stop, step)]
    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc")
    plt.ylabel("time")
    plt.plot(x_axis, selection_time, '+',color='b', label='selection sort')
    plt.plot(x_axis, insertion_time, '+',color='g', label='insertion sort')
    plt.plot(x_axis, bubbls_time, '+',color='r', label='bubbl sort')
    plt.legend()
    plt.show()

    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc in log")
    plt.ylabel("time in log")
    logX = [math.log(x) for x in x_axis]
    log_selection_time = [math.log(y) for y in selection_time]
    log_insertion_time = [math.log(y) for y in insertion_time]
    log_bubbls_time = [math.log(y) for y in bubbls_time]

    ms , ks = lin_reg(logX, log_selection_time)
    mi , ki = lin_reg(logX, log_insertion_time)
    mb , kb = lin_reg(logX, log_bubbls_time)

    lineY_s = [(ms + x * ks) for x in logX]
    lineY_i = [(mi + x * ki) for x in logX]
    lineY_b = [(mb + x * kb) for x in logX]

    plt.plot(logX, log_selection_time, '+',color='b', label=f'selection sort: k= {ks}')
    plt.plot(logX, log_insertion_time, '+',color='g', label=f'insertion sort: k= {ki}')
    plt.plot(logX, log_bubbls_time, '+',color='r', label=f'bubbl sort: k= {kb}')
    plt.plot(logX,lineY_s, '-',color='b')
    plt.plot(logX,lineY_i, '-',color='g')
    plt.plot(logX,lineY_b,'-',color='r')
    plt.legend()
    plt.show()

# n*log(n) test values
start = 100000
stop = 5000001
step = 100000
prsison = 5
with_merge_sort = False

def vis_nlogn():
    x_axis = [*range(start, stop, step)]
    
    if with_merge_sort == True:
        merge_time = test(sa.merge_sort)
        plt.plot(x_axis, median_time, '+',color='r', label='median quicksort')
    
    quick_time = test(sa.quick_sort)
    median_time = test(sa.quick_median_sort)
    
    plt.xlabel(f"iterration from {start} to {stop} in {step} distanc")
    plt.ylabel("time")
    plt.plot(x_axis, merge_time, '+',color='b', label='merge sort')
    plt.plot(x_axis, quick_time, '+',color='g', label='quick sort')
    plt.legend()
    plt.show()


vis_nlogn()
#vis_n_2()