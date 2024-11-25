import matplotlib.pyplot as plt
import linear_regression as linreg


def plotting(X, Y):  # Size = X Averages = Y
    plt.subplot(121)
    plt.plot(X, Y, 'o')
    plt.xlabel("List Size")
    plt.ylabel("Average Time")
    linreg.calc_regress(X, Y)
