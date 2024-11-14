def pascal_line(n):
    lst = []
    lst = pascal_rec(lst, n)
    return lst


def pascal_rec(lst, n):
    if n == 0:
        lst.append(1)
        return lst
    else:
        new_lst = []
        lst = pascal_rec(lst, n - 1)
        n -= 1
        for i in range(len(lst) - 1):
            new_lst.append(lst[i] + lst[i + 1])
        new_lst.insert(0, 1)
        new_lst.append(1)
        return new_lst


print(pascal_line(3))
