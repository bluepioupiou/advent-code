from utils import log, Grid, Position, DIRECTIONS
from itertools import combinations

file = open('8.txt', 'r')
lines = file.readlines()

total = 0
antenna_types = {}
antinodes = set()
if __name__ == '__main__':
    grid = Grid(lines)
    log(grid)
    for char, position in grid.scan():
        if char != ".":
            if char not in antenna_types:
                antenna_types[char] = []
            antenna_types[char].append(position)
    log(antenna_types)
    for positions in antenna_types.values():
        for position1, position2 in list(combinations(positions, 2)):
            distance1 = position1.distance(position2)
            antinode1 = position2.move_with_direction(distance1)
            while grid.has(antinode1):
                antinodes.add(antinode1)
                antinode1 = antinode1.move_with_direction(distance1)

            distance2 = position2.distance(position1)
            antinode2 = position1.move_with_direction(distance2)
            while grid.has(antinode2):
                antinodes.add(antinode2)
                antinode2 = antinode2.move_with_direction(distance2)

    for antinode in antinodes:
        grid.replace(antinode, "#")
    log(grid)
    for char, position in grid.scan():
        if char != ".":
            total += 1
    print(total)

