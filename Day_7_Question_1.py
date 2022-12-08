import re

class Directory:
    def __init__(self, dir_name, orgin_dir):
        self.name = dir_name
        self.orgin = orgin_dir
        self.dep_dirs = []
        self.dep_files = []
        self.file_sum = 0

    def __str__(self) -> str:
        return(f"directory: {self.name}\norgin directory: {self.orgin}\ndirs: {self.dep_dirs}\nfiles: {self.dep_files}")

    def read_contents(self, dirs, files):
        for dir in dirs:
            self.dep_dirs.append(Directory(dir, self))
            dir_list.append(Directory(dir, self))
        for file in files:
            self.dep_files.append(File(file))

    def go_to_orgin(self):
        return self.orgin

    def open_dir(self, dir_open):
        for dir in self.dep_dirs:
            if dir_open == dir.name:
                return dir
    
    def find_size(self):
        tempsum = 0
        for file in self.dep_files:
            tempsum = tempsum + file.size
        for dir in self.dep_dirs:
            tempsum = tempsum + dir.find_size()
        file_sizes.append(tempsum)
        return tempsum

class File:
    def __init__(self, file_size, file_name) -> None:
        self.size = int(file_size)
        self.name = file_name

    def __str__(self) -> str:
        return(f"file name: {self.name}\nsize: {self.size}")

def process_lines(lines):
    commands = []
    for line in lines:  
        change_dir = re.findall("\$ (cd) (.+)", line)
        list = re.findall("\$ (ls)", line)
        dir = re.findall("(dir) (.+)", line)
        file = re.findall("(\d+) (.+)", line)
        if change_dir:
            commands.append(change_dir)
        elif list:
            commands.append(list)
        elif dir:
            commands.append(dir)
        elif file:
            commands.append(file)
    return commands

def run_command(line):
    command = line[0][0]
    info = line[0][1]
    if command == "cd":
        if info == "..":
            global current_dir
            current_dir = current_dir.go_to_orgin()
        else:
            current_dir = current_dir.open_dir(info)
    elif command == "dir":
        current_dir.dep_dirs.append(Directory(info, current_dir))
        dir_list.append(Directory(info, current_dir))
    elif command == "l":
        print(command)
    else:
        current_dir.dep_files.append(File(command, info))

with open("E:\Code\Coding\Advent of Code 2022\Day_7_Input.txt", "r") as input:
    lines = input.readlines()

lines = process_lines(lines=lines)
base_dir = Directory("/", None)
current_dir = base_dir
dir_list = [base_dir]

i = 1
while i < len(lines):
    run_command(lines[i])
    i += 1

file_sizes = []
base_dir.find_size()

output = 0
for file_size in file_sizes:
    if file_size < 100000:
        output += file_size

print(output)
