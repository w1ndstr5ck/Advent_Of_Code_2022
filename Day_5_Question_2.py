import re
import pandas as pd
import numpy as np

with open("E:\Code\Coding\Advent of Code 2022\Day_5_Input.txt", "r") as file:
    lines = file.readlines()

OG_state_lines = lines[0:8]
Command_Lines = lines[10:]

state = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}

def load_state_lines(state_lines):
    rows = []
    for line in state_lines:
        line = line.strip()
        rows.append(re.split(".(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.).", line)[1:10])
    return(rows)

def load_commands(command_lines):
    commands = []
    for line in command_lines:
        line = line.strip()
        commands.append(re.split("move (\d{1,2}) from (\d{1,2}) to (\d{1,2})", line)[1:4])
    return commands

def load_state(state_rows):
    state_rows.reverse()
    for row in state_rows:
        i = 0
        while i <= 8:
            if row[i] != " ":
                state[i+1].append(row[i])
                i += 1
            else:
                i += 1

def move(number_to_move, from_row, to_row):
    elements = state[from_row][-number_to_move:]
    state[from_row] = state[from_row][:-number_to_move]
    state[to_row].extend(elements)

def execute_commands(commands):
    for command in commands:
        move(number_to_move=int(command[0]), from_row=int(command[1]), to_row=int(command[2]))

def print_out():
    output_string = ""
    for stack in state:
        output_string = output_string + state[stack][-1]
    return output_string

load_state(load_state_lines(OG_state_lines))
execute_commands(load_commands(command_lines=Command_Lines))
print(print_out())


#PSNRGBTFT