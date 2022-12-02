
file_name = "E:\Code\Coding\Advent of Code 2022\Day_1_Question_1_Input.txt"
elf = {"elf number" : 1,
    "calories" : 0}
elfs = []

with open(file_name, "r") as input:
    lines = input.readlines()

for line in lines:
    if line == "\n":
        elfs.append(elf.copy())
        elf["elf number"] += 1
        elf["calories"] = 0
    else:
        elf["calories"] += int(line)
    
top_elfs = [0]
for e in elfs:
    if e["calories"] > top_elfs[0]:
        top_elfs.insert(0, e["calories"])
    elif e["calories"] > top_elfs[1]:
        top_elfs.insert(1, e["calories"])
    elif e["calories"] > top_elfs[2]:
        top_elfs.insert(2, e["calories"])

print(elfs)
print(top_elfs)
print(sum(top_elfs[0:3]))