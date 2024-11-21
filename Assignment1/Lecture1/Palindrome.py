def rec_palindrom(x):
    if len(x) == 1 or 0:
        return True
    elif len(x) == 2:
        if x[0] == x[1]:
            return True
        else:
            return False
    else:
        if rec_palindrom(x[1:-1]) is True:
            return True
        else:
            return False


print(rec_palindrom('anna'))
