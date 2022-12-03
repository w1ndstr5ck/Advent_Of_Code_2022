import string

with open("E:\Code\Coding\Advent of Code 2022\Day_3_Input.txt", "r") as input:
    rucksacks = input.readlines()

#Clear the \n from each line.
new_ruck = []
for rucksack in rucksacks:
    new_ruck.append(rucksack.strip())

#Find the items that are in both compartments of the rucksack.
error_items = []
for rucksack in new_ruck:
    half_way = int(len(rucksack)/2)
    first_half = rucksack[:half_way]
    second_half = rucksack[half_way:]
    for i in first_half:
        if i in second_half:
            error_items.append(i)
            break

#Create lookup table for each item
item_priority = {}
for i in range(0, 52):
    item_priority[string.ascii_letters[i]] = i+1

#Lookup each error item in the lookup table and add the value to the output
priorities = 0
for items in error_items:
    priorities = priorities + item_priority[items]

print(priorities)
#print(item_priority)
#print(len(error_items))

