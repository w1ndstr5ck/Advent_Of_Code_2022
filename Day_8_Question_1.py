import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt

def is_visable(row, col, data):
    if is_visable_left(row, col, data) or is_visable_right(row, col, data) or is_visable_up(row, col, data) or is_visable_down(row, col, data):
        return True
    else:
        return False

def is_visable_left(row, col, data):
    if col == 0:
        return True
    height = data[row, col]
    trees = data[row, 0:col]
    for tree in trees:
        if tree >= height:
            return False
    return True

def is_visable_right(row, col, data):
    if col == 98:
        return True
    height = data[row, col]
    trees = data[row, col+1:99]
    trees = list(trees)
    for tree in trees:
        if tree >= height:
            return False
    return True

def is_visable_up(row, col, data):
    if row == 0:
        return True
    height = data[row,col]
    trees = data[0:row, col]
    for tree in trees:
        if tree >= height:
            return False
    return True

def is_visable_down(row, col, data):
    if row == 98:
        return True
    height = data[row,col]
    trees = data[row+1:99, col]
    for tree in trees:
        if tree >= height:
            return False
    return True

with open("E:\Code\Coding\Advent of Code 2022\Day_8_Input.txt", "r") as input:
    lines = input.readlines()

forest_df = pd.DataFrame()
i = 0
while i < len(lines):
    line = re.findall("(\d)", lines[i])
    int_line = []
    for char in line:
        int_line.append(int(char))
    forest_df[f"{i}"] = int_line
    i += 1

forest_array = np.array(forest_df.transpose())
print(forest_array)
visable_count = 0

x = []
y = []


r = 0
while r < 99:
    c = 0
    while c < 99:
        if is_visable(r, c, forest_array):
            x.append(r)
            y.append(c)
            visable_count = visable_count + 1
            c += 1
        else:
            c += 1
    r += 1


print(visable_count)

plt.rcParams["figure.figsize"] = [99, 99]
plt.rcParams["figure.autolayout"] = True
plt.xlim(0, 99)
plt.ylim(0, 99)
plt.grid()
plt.plot(x, y, marker="s", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.show()
