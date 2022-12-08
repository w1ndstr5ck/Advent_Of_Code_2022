import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt

def is_visable(row, col, data):
    output = is_visable_left(row, col, data)
    output = output * is_visable_right(row, col, data)
    output = output * is_visable_up(row, col, data)
    output = output * is_visable_down(row, col, data)
    return output
        

def is_visable_left(row, col, data):
    view_score = 0
    if col == 0:
        return 0
    height = data[row, col]
    trees = data[row, 0:col]
    trees = list(trees)
    for tree in reversed(trees):
        if tree >= height:
            return view_score + 1
        else:
            view_score = view_score + 1
    return view_score

def is_visable_right(row, col, data):
    view_score = 0
    if col == 98:
        return 0
    height = data[row, col]
    trees = data[row, col+1:99]
    for tree in trees:
        if tree >= height:
            return view_score + 1
        else:
            view_score = view_score + 1
    return view_score

def is_visable_up(row, col, data):
    view_score = 0
    if row == 0:
        return 0
    height = data[row,col]
    trees = data[0:row, col]
    trees = list(trees)
    for tree in reversed(trees):
        if tree >= height:
            return view_score + 1
        else:
            view_score = view_score + 1
    return view_score

def is_visable_down(row, col, data):
    view_score = 0
    if row == 98:
        return 0
    height = data[row,col]
    trees = data[row+1:99, col]
    for tree in trees:
        if tree >= height:
            return view_score + 1
        else:
            view_score = view_score + 1
    return view_score

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

is_visable(74,64,forest_array)

solution = 0

r = 0
while r < 99:
    c = 0
    while c < 99:
        if is_visable(r, c, forest_array) > solution:
            solution = is_visable(r, c, forest_array)
            print(f'{r}, {c}')
            c += 1
        else:
            c += 1
    r += 1

print(solution)

