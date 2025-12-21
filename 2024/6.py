import re
file = open('6.txt', 'r')
lines = file.readlines()

total = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
distincts = set()
position = None
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "^":
            position = (row, col)
            distincts.add(position)
            lines[row] = line.replace("^", ".")
            break
    if position:
        break

while 0 < position[0] < len(lines) - 1 and 0 < position[1] < len(lines[-1]) - 1:
    new_position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
    if lines[new_position[0]][new_position[1]] != ".":
        direction = (direction + 1) % 4
        print(f"Turn {direction}")
    else:
        position = new_position
        distincts.add(position)
        print(position)


print(len(distincts))
