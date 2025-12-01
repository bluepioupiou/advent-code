from utils import log, Grid, Position, DIRECTIONS
from itertools import combinations

file = open('9.txt', 'r')
lines = file.readlines()

total = 0
if __name__ == '__main__':
    line = lines[0]
    block_string = []
    block_ID = 0
    block_data = True
    for char in line:
        if block_data:
            block_string += [block_ID] * int(char)
            block_ID += 1
        else:
            block_string += ["."] * int(char)
        block_data = not block_data
    log(block_string)
    while True:
        for index, char in enumerate(reversed(block_string), 1):
            if char != ".":
                index_char = len(block_string) - index
                #log(block_string[start + len(block) - index])
                space_index = block_string.index(".")
                if space_index > index_char:
                    break
                block_string = block_string[:space_index] + [char] + block_string[space_index + 1:index_char] + ["."] + block_string[index_char+1:]
                #log(block_string)
        else:
            continue
        break
    log(block_string)
    for index, char in enumerate(block_string):
        if char != ".":
            total += index * int(char)

    print(total)