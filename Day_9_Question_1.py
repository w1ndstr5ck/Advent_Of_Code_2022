import numpy as np

def go_up(units):
    i = 0
    while i < units:
        moved_val = pos_dict["H"]["vert_pos"] + 1
        if dis_over_2(pos_dict["H"]["hor_pos"], moved_val):
            pos_dict["T"]["hor_pos"] = pos_dict["H"]["hor_pos"]
            pos_dict["T"]["vert_pos"] = pos_dict["H"]["vert_pos"]
            has_been_array[pos_dict["T"]["hor_pos"]][pos_dict["T"]["vert_pos"]] = True
        pos_dict["H"]["vert_pos"] = moved_val
        i += 1

def go_down(units):
    i = 0
    while i < units:
        moved_val = pos_dict["H"]["vert_pos"] - 1
        if dis_over_2(pos_dict["H"]["hor_pos"], moved_val):
            pos_dict["T"]["hor_pos"] = pos_dict["H"]["hor_pos"]
            pos_dict["T"]["vert_pos"] = pos_dict["H"]["vert_pos"]
            has_been_array[pos_dict["T"]["hor_pos"]][pos_dict["T"]["vert_pos"]] = True
        pos_dict["H"]["vert_pos"] = moved_val
        i += 1

def go_left(units):
    i = 0
    while i < units:
        moved_val = pos_dict["H"]["hor_pos"] - 1
        if dis_over_2(moved_val, pos_dict["H"]["vert_pos"]):
            pos_dict["T"]["hor_pos"] = pos_dict["H"]["hor_pos"]
            pos_dict["T"]["vert_pos"] = pos_dict["H"]["vert_pos"]
            has_been_array[pos_dict["T"]["hor_pos"]][pos_dict["T"]["vert_pos"]] = True
        pos_dict["H"]["hor_pos"] = moved_val
        i += 1

def go_right(units):
    i = 0
    while i < units:
        moved_val = pos_dict["H"]["hor_pos"] + 1
        if dis_over_2(moved_val, pos_dict["H"]["vert_pos"]):
            pos_dict["T"]["hor_pos"] = pos_dict["H"]["hor_pos"]
            pos_dict["T"]["vert_pos"] = pos_dict["H"]["vert_pos"]
            has_been_array[pos_dict["T"]["hor_pos"]][pos_dict["T"]["vert_pos"]] = True
        pos_dict["H"]["hor_pos"] = moved_val
        i += 1

def dis_over_2(head_vert, head_hor):
    if abs(head_vert - pos_dict["T"]["hor_pos"]) >= 2:
        return True
    if abs(head_hor - pos_dict["T"]["vert_pos"]) >= 2:
        return True
    if abs(head_vert - pos_dict["T"]["hor_pos"]) + abs(head_hor - pos_dict["T"]["vert_pos"]) >= 2:
        return True

#Input data
with open("E:\Code\Coding\Advent of Code 2022\Day_9_Input.txt", "r") as input:
    commands = input.readlines()

#Create a 400 x 250 array full of False values and assign it to has_been_array
has_been_array = np.full((400, 250), False, bool)
#Assign the current possition in the array of both the head and the tail to the orgin 75, 125
pos_dict = {
    "H" : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    "T" : {
        "hor_pos" : 75,
        "vert_pos" : 125
    }
}

has_been_array[pos_dict["T"]["hor_pos"]][pos_dict["T"]["vert_pos"]] = True

#Create a new list of length 2 lists to store the commands
commands_list = []
#Loop though all of the commands and split them on the " " in the center providing a length 2 list with the direction and then the number of possitions to move
for command in commands:
    commands_list.append(command.split())


for command in commands_list:
    if command[0] == "U":
        check_val = go_up(int(command[1]))
    elif command[0] == "D":
        check_val = go_down(int(command[1]))
    elif command[0] == "L":
        check_val = go_left(int(command[1]))
    elif command[0] == "R":
        check_val = go_right(int(command[1]))
    
print(pos_dict)

z = 0
a = []
b = []
for x in has_been_array:
    for y in x:
        if y == True:
            a.append(x)
            z = z + 1

print(z)

#guess 1: 6435 too high
#guess 2: 6354 correct