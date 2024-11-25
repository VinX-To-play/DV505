import random as rnd
import matplotlib as mpl


def small_list(size):
    lst = []
    for n in range(size):
        lst.append(rnd.randint(-10, 10))
    print(lst)
    return lst


def simple_sum(lst):
    tgt = 0  # Target to sum towards
    triples = set()  # Saving unique pairs
    for n in range(len(lst)-1):
        num1 = lst[n]
        for i in range(n+1, len(lst)):
            num2 = lst[i]
            for o in range(i+1, len(lst)):
                num3 = lst[o]
                if num1 + num2 + num3 == tgt: 
                    triples.add(tuple(sorted([num1, num2, num3])))
    return list(triples)


#print(simple_sum(small_list(10)))
lst = [-7, 10, 8, -6, -2, 3, -2, 6, 3, 10]
print(simple_sum(lst))