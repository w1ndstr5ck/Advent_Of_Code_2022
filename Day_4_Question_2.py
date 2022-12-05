with open("E:\Code\Coding\Advent of Code 2022\Day_4_Input.txt", "r") as data:
    data_in = data.readlines()

count = 0
for pair in data_in:
    pairs = pair.split(",")
    first_pair = pairs[0].split("-")
    second_pair = pairs[1].strip("\n").split("-")
    first_list = list(range(int(first_pair[0]), int(first_pair[1])+1))
    second_list = list(range(int(second_pair[0]), int(second_pair[1])+1))
    if any(elem in first_list for elem in second_list): 
        count += 1

print(count)
