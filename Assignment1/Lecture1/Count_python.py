import os
path = '/home/vincentl/Documents/LNU/DV505/'

def count_lines(path, depth = 0):
    try:
        dir_list = os.listdir(path)

        for e in dir_list:
            if str(e)[-3::] == '.py':
                print('     ' * depth, calc_full_lin_py(e))
            else:
                print('     ' * depth, e)
            count_lines(path + e + '/', depth + 1)
    except:
        return

def calc_full_lin_py(path):
    total_full_line = 0
    with open(path, 'r') as file:
        lins = file.readlines()
        print(lins)


count_lines(path)