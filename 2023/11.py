import re
import functools
file = open('11.txt', 'r')
lines = file.readlines()


total = 0
empty_rows = []
empty_cols = []

print(f"Grid with {len(lines)} rows and {len(lines[0].strip())} cols")

for row, line in enumerate(lines):
    line = line.rstrip()
    if "#" not in line:
        empty_rows.append(row)
print(f"Empty rows {empty_rows}")

for col in range(len(lines[0].strip())):
    for row, line in enumerate(lines):
        if "#" == line[col]:
            break
    else:
        empty_cols.append(col)
print(f"Empty cols {empty_cols}")

galaxies = []
for row, line in enumerate(lines):
    for col, point in enumerate(line):
        if point == "#":
            galaxies.append((row, col))
print(f"Galaxies {galaxies}")

for galaxy_1 in galaxies:
    for galaxy_2 in galaxies:
        if galaxy_1 != galaxy_2:
            distance = abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])
            #print(f"Galaxy 1 : {galaxy_1} et galaxy 2 : {galaxy_2} --> distance {distance}")
            add_row = 999999 * len(list(filter(lambda x: min(galaxy_1[0], galaxy_2[0]) < x < max(galaxy_1[0], galaxy_2[0]), empty_rows)))
            add_col = 999999 * len(list(filter(lambda x: min(galaxy_1[1], galaxy_2[1]) < x < max(galaxy_1[1], galaxy_2[1]), empty_cols)))
            total += distance + add_row + add_col
total /= 2
print(f"Solution {total}")
