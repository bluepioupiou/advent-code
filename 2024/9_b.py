from utils import log, Grid, Position, DIRECTIONS
from itertools import combinations

file = open('9.txt', 'r')
lines = file.readlines()

total = 0
if __name__ == '__main__':
    line = lines[0]
    file_system = []
    block_ID = 0
    block_data = True
    files = []
    frees = []
    #log(line)
    for char in line:
        if block_data:
            files.append({
                "id": str(block_ID),
                "start": len(file_system),
                "len": int(char)
            })
            file_system += [block_ID] * int(char)
            block_ID += 1
        else:
            frees.append({
                "start": len(file_system),
                "len": int(char)
            })
            file_system += ["."] * int(char)

        block_data = not block_data
    #log(files)
    #log(frees)
    #log(file_system)
    for file in reversed(files):
        #log(f"Testing {file}")
        for index, free in enumerate(frees):
            #log(f" - Testing {free}")
            if free["len"] >= file["len"] and free["start"] < file["start"]:
                log(f"Found free space for {file} at {free}")
                file_system = file_system[:free["start"]] + \
                              [file["id"]] * file["len"] + \
                              ["."] * (free["len"] - file["len"]) + \
                              file_system[free["start"] + free["len"]:file["start"]] + \
                              ["."] * file["len"] + \
                              file_system[file["start"] + file["len"]:]
                frees[index] = {
                    "len": free["len"] - file["len"],
                    "start": free["start"] + file["len"]
                }
                #log(file_system)
                break
    #log(file_system)
    for index, char in enumerate(file_system):
        if char != ".":
            total += index * int(char)

    print(total)
