import numpy as np
from matplotlib import pyplot as plt

def move_tail(index, moved_vert, moved_hor):
    #Need to change the values before calling them again
    i = index
    if i < 10:
        if dis_over_2(moved_vert, moved_hor, pos_dict[i]["vert_pos"], pos_dict[i]["hor_pos"]):
            moved_vert = pos_dict[i-1]["vert_pos"]
            moved_hor = pos_dict[i-1]["hor_pos"]
            move_tail(i+1, moved_vert, moved_hor)
            pos_dict[i]["vert_pos"] = moved_vert
            pos_dict[i]["hor_pos"] = moved_hor
            has_been_array[pos_dict[9]["vert_pos"]][pos_dict[9]["hor_pos"]] = True
            #x.append(pos_dict[9]["vert_pos"])
            #y.append(pos_dict[9]["hor_pos"])
            #n.append(len(y))
            #print(f"Moved: {index} moving to {moved_vert}, {moved_hor}")
        #else:
            #print(f"Skipped: {index} moving to {moved_vert}, {moved_hor}")

def go_up(units):
    i = 0
    while i < units:
        moved_vert = pos_dict[0]["vert_pos"] + 1
        moved_hor = pos_dict[0]["hor_pos"]
        move_tail(index=1, moved_vert=moved_vert, moved_hor=moved_hor)
        pos_dict[0]["vert_pos"] = moved_vert
        i += 1

def go_down(units):
    i = 0
    while i < units:
        moved_vert = pos_dict[0]["vert_pos"] - 1
        moved_hor = pos_dict[0]["hor_pos"]
        move_tail(index=1, moved_vert=moved_vert, moved_hor=moved_hor)      
        pos_dict[0]["vert_pos"] = moved_vert
        i += 1

def go_left(units):
    i = 0
    while i < units:
        moved_vert = pos_dict[0]["vert_pos"]
        moved_hor = pos_dict[0]["hor_pos"] - 1
        move_tail(index=1, moved_vert=moved_vert, moved_hor=moved_hor)   
        pos_dict[0]["hor_pos"] = moved_hor
        i += 1

def go_right(units):
    i = 0
    while i < units:
        moved_vert = pos_dict[0]["vert_pos"]
        moved_hor = pos_dict[0]["hor_pos"] + 1
        move_tail(index=1, moved_vert=moved_vert, moved_hor=moved_hor)         
        pos_dict[0]["hor_pos"] = moved_hor
        i += 1

def dis_over_2(head_vert, head_hor, tail_vert, tail_hor):
    if abs(tail_vert - head_vert) >= 2:
        return True
    if abs(head_hor - tail_hor) >= 2:
        return True
    return False

#Input data
with open("E:\Code\Coding\Advent of Code 2022\Day_9_Input.txt", "r") as input:
    commands = input.readlines()

#Create a 400 x 250 array full of False values and assign it to has_been_array
has_been_array = np.full((400, 400), False, bool)
#Assign the current possition in the array of both the head and the tail to the orgin 75, 125
pos_dict = {
    0 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    1 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    2 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    3 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    4 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    5 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    6 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    7 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    8 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    },
    9 : {
        "hor_pos" : 75,
        "vert_pos" : 125
    }
}

#has_been_array[pos_dict[9]["hor_pos"]][pos_dict[9]["vert_pos"]] = True

#Create a new list of length 2 lists to store the commands
commands_list = []
#Loop though all of the commands and split them on the " " in the center providing a length 2 list with the direction and then the number of possitions to move
for command in commands:
    commands_list.append(command.split())

x = []
y = []
n = []

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
r = 0
while r < 400:
    c = 0
    while c < 400:
        if has_been_array[r][c]:
            z = z + 1
            c += 1
        else:
            c += 1
    r += 1

print(z)


'''plt.rcParams["figure.figsize"] = [99, 99]
plt.rcParams["figure.autolayout"] = True
plt.xlim(0, 400)
plt.ylim(0, 250)
plt.grid()
for i, txt in enumerate(n):
    plt.annotate(txt, (x[i], y[i]))
plt.plot(x, y, marker="s", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.show()'''
