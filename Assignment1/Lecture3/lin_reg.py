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