import math
import matplotlib.pyplot as plt


def calc_regress(X, Y):  # Calculates the linear regression and plots it
    logX = [math.log(x) for x in X]
    logY = [math.log(y) for y in Y]
    m, k = lin_reg(logX, logY)
    lineY = [m + k*x for x in logX]
    plt.subplot(122)
    plt.plot(logX, logY, "x", logX, lineY, "red")
    plt.show()


def lin_reg(logX, logY):  # Formulates the linear regresssion
    s_of_x = sum(logX)
    s_of_y = sum(logY)
    s_of_x2 = square_sum(logX)
    s_of_xy = sum_xy(logX, logY)

    m = ((s_of_x2*s_of_y) - (s_of_x * s_of_xy)) / ((len(logX) * s_of_x2) - (s_of_x * s_of_x))
    k = ((len(logX) * s_of_xy) - (s_of_x * s_of_y)) / ((len(logX) * s_of_x2) - (s_of_x * s_of_x))
    print(f"m is {m}, k is {k}")
    return m, k


def square_sum(lst):  # Squares each entry and adds them
    total = 0
    for i in lst:
        total = total + i**2
    return total


def sum_xy(x, y):  # Multiplies X with Y and adds them
    total = 0
    for m, n in zip(x, y):
        total = total + m * n
    return total
