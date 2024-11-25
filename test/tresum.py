import random as rnd
import time
import plotting as plot


def generate_list(size):  # Runs the brute force after
    lst = []
    for n in range(size):
        lst.append(rnd.randint(-1 * size, size))
        lst = sorted(lst)
    return lst


def brute_3sum(lst):  # Sums up the list
    tgt = 0  # Target to sum towards
    triples = set()  # Saving unique pairs
    for n in range(len(lst) - 2):
        #num1 = lst[n]
        for i in range(n+1, len(lst) - 1):
            #num2 = lst[i]
            for o in range(i+1, len(lst)):
                #num3 = lst[o]
                if lst[n] + lst[i] + lst[o] == tgt:
                    triples.add((lst[n], lst[i], lst[o]))
    return triples


def repeat_runs(lst):
    before = time.time()
    brute_3sum(lst)
    elapsed = time.time() - before
    return elapsed


def experiment():
    print("Experiment Start!")
    size = []  # Store sizes
    time_elapsed = []  # Stores time per run
    averages = []  # Stores all averages
    repeat = 5
    average_time = 0
    for sz in range(50, 451, 25):
        size += [sz]
        for run in range(repeat+1):
            lst = generate_list(sz)
            time_elapsed.append(repeat_runs(lst))
        total_time = sum(time_elapsed)
        average_time = total_time / repeat
        averages.append(average_time)
        print(f"Average time for size {sz}: {average_time} seconds, for a total of {total_time} seconds.")
    print("Finished runs! Printing graph")
    plot.plotting(size, averages)


experiment()
