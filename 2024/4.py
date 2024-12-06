import re
file = open('4.txt', 'r')
lines = file.readlines()

total = 0
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]
total_rows = len(lines)
total_cols = len(lines[-1])
total_positions = []
#print(total_rows, total_cols)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        #print(f"found X at {row}, {col}")
        for direction in directions:
            #print(f"trying direction {direction}")
            word = lines[row][col]
            next_pos = (row, col)
            positions = [next_pos]
            for index in range(3):
                next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
                positions.append(next_pos)
                #print(f"inspecting {next_pos[0]}, {next_pos[1]} for {search}")
                if next_pos[0] >= total_rows or next_pos[1] >= total_cols:
                    break
                next_char = lines[next_pos[0]][next_pos[1]]
                word += next_char
            else:
                if word == "XMAS":
                    total += 1
                    total_positions += positions


for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if (row, col) not in total_positions:
            lines[row] = lines[row][:col] + "." + lines[row][col+1:]

for line in lines:
    print(line)
print(total)
