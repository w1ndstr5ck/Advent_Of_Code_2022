import numpy as np

with open("E:\Code\Coding\Advent of Code 2022\Day_6_Input.txt", "r") as data:
    data = data.readline()

def find_marker(datastream):
    i = 3
    while i < len(datastream):
        check_vector = [datastream[i], datastream[i-1], datastream[i-2], datastream[i-3]]
        print(set(check_vector))
        if len(set(check_vector)) == len(check_vector):
            return i + 1
        else:
            i += 1
        

print(find_marker(datastream=data))