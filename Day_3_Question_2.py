import string

with open("E:\Code\Coding\Advent of Code 2022\Day_3_Input.txt", "r") as input:
    rucksacks = input.readlines()

#Clear the \n from each line.
new_ruck = []
for rucksack in rucksacks:
    new_ruck.append(rucksack.strip())

#Create lists of lists of strings with each element of the string being a different group
groups = []
while len(new_ruck) > 0:
    group = []
    for i in range(0, 3):
        group.append(new_ruck.pop())
    groups.append(tuple(group))

#Loop in each group and check if each character in the first rucksack of the group is contained in both the second and third rucksack.
#If so return the char to the list badges to be used later in the lookup table.
badges = []    
for group in groups:
    for char in group[0]:
        if char in group[1]:
            if char in group[2]:
                badges.append(char)
                break

#Create lookup table for each item
item_priority = {}
for i in range(0, 52):
    item_priority[string.ascii_letters[i]] = i+1

#Lookup each badge in the lookup table and add the value to the output
priorities = 0
for badge in badges:
    priorities = priorities + item_priority[badge]

print(priorities)


    

