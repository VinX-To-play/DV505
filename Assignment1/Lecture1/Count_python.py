import os
path = '/home/vincentl/Documents/LNU/DV505/Assignment1'

def count_lines(path, depth):
    try:
        dir_list = os.listdir(path)
        