#O(n^2) Algoritems
# Selection sort
def selection_sort(lst):
    length = len(lst)
    if length == 0: return lst
    lowist = lst[0]
    lowist_index = 0
    pos = 0
    while pos < length:
        for i in range(pos, length):
            if lst[i] < lowist:
                lowist = lst[i]
                lowist_index = i
        lst[pos], lst[lowist_index] = lst[lowist_index] , lst[pos]
        pos += 1
        if pos < length:
            lowist = lst[pos]
            lowist_index = pos
    return lst
        
# Insertion Sort
def insertion_sort(lst: list):
    object_index = 1
    for index in range(len(lst) - 1):      
        if lst[object_index] < lst[index]:
            while lst[object_index] < lst[index]:
                if index > 0:
                    index -= 1
                elif index == 0: break
            obj = lst[object_index]
            lst.pop(object_index)
            lst.insert(index, obj)
        object_index += 1
    return lst

# Bubble Sort
def bubble_sort(lst: list):
    swop = 1
    while swop > 0:
        swop = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swop += 1
    return lst

# O(n*log(n)) Algoritems
# Merge Sort
def merge_sort(lst:list):
    if len(lst) <= 1: return lst
    else:
        mid = len(lst) // 2
        left = lst[0:mid]
        right = lst[mid:len(lst)]

        left_lst = merge_sort(left)
        right_lst = merge_sort(right)

        l, r, = 0 , 0
        combind_lst = []
        left_lst_length = len(left_lst)
        right_lst_length = len(right_lst)


        while l < left_lst_length and r < right_lst_length:
            if left_lst[l] <= right_lst[r]:
                combind_lst += [left_lst[l]]
                l += 1
            else:
                combind_lst += [right_lst[r]]
                r += 1
        if l != left_lst_length:
            combind_lst += left_lst[l::]
        if r != right_lst_length:
            combind_lst += right_lst[r::]
        return combind_lst 

# Quick Sort 
def quick_sort(lst:list):
    # Base case
    if len(lst) <= 1: return lst
    # set var
    pivit = [lst[0]]
    left = []
    right = []

    # split left, right
    for e in lst[1::]:
        if e < pivit[0]:
            left.append(e)
        elif e > pivit[0]:
            right.append(e)
        else:
            pivit.append(e)

    return quick_sort(left) + pivit + quick_sort(right)     

#quick median sort
def quick_median_sort(lst:list):
    lst_length = len(lst)
    # Base case
    if lst_length <= 1: return lst
    # set var
    if lst_length >= 3:
        pivit = [lst[0] , lst[lst_length - 1] , lst[(lst_length - 1)]][1]
    else:
        pivit = lst[2]
    pivit_in_lst = []
    left = []
    right = []

    # split left, right
    for e in lst[1::]:
        if e < pivit:
            left.append(e)
        elif e > pivit:
            right.append(e)
        else:
            pivit_in_lst.append(e)

    return quick_sort(left) + pivit_in_lst + quick_sort(right)   