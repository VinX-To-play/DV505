import os

path = '/home/vincentl/Documents/LNU/DV505/'

def print_directory(path):
    try:
        dir_list = os.listdir(path)
        print(dir_list)
        for e in dir_list:
            print_directory(path + e + '/')
    except:
        return


print_directory(path)
