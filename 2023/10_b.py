import re
import functools
file = open('10.txt', 'r')
lines = file.readlines()


class Pipe:
    def __init__(self, type, connections):
        self.type = type
        self.connections = connections

    def __str__(self):
        return f"Pipe {self.type} with connections {self.connections}"

    def __repr__(self):
        return f"Pipe({self.type}, {self.connections})"


class Tile:
    def __init__(self, pipe, position, origin):
        self.pipe = pipe
        self.position = position
        self.origin = origin

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f"Tile on {self.position} with pipe {self.pipe} and origin {self.origin}"

    def __repr__(self):
        return f"Tile({self.position}, {self.pipe}, {self.origin})"

    def get_next_tile(self):
        # print(self)
        origin_direction = (self.origin[0] - self.position[0], self.origin[1] - self.position[1])
        next_tile_direction = next(filter(lambda x: x != origin_direction, self.pipe.connections))
        # print(next_tile_direction)
        next_tile_position = (self.position[0] + next_tile_direction[0], self.position[1] + next_tile_direction[1])
        # print(next_tile_position)
        next_tile_type = lines[next_tile_position[0]][next_tile_position[1]]
        # print(next_tile_type)
        next_tile_pipe = next(filter(lambda x: x.type == next_tile_type, pipes))
        return Tile(next_tile_pipe, next_tile_position, self.position)


def replace_at_position_by(grid, row, col, replacement):
    grid[row] = grid[row][:col] + replacement + grid[row][col + 1:]


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pipes = [
    Pipe("F", [(1, 0), (0, 1)]),
    Pipe("7", [(0, -1), (1, 0)]),
    Pipe("J", [(0, -1), (-1, 0)]),
    Pipe("L", [(0, 1), (-1, 0)]),
    Pipe("-", [(0, -1), (0, 1)]),
    Pipe("|", [(-1, 0), (1, 0)])
]
total = 0

starting_position = None
for row, line in enumerate(lines):
    if "S" in line:
        starting_position = (row, line.index("S"))
        break
print(f"Starting position {starting_position}")

neighbors = []
for direction in directions:
    neighbour_position = (
        min(len(lines), max(0, starting_position[0] + direction[0])),
        min(len(lines[0]), max(0, starting_position[1] + direction[1]))
    )
    neighbour_type = lines[neighbour_position[0]][neighbour_position[1]]
    if neighbour_type != "." and neighbour_type != "S":
        pipe = next(filter(lambda x: x.type == neighbour_type, pipes))
        if (-direction[0], -direction[1]) in pipe.connections:
            neighbors.append(Tile(pipe, neighbour_position, starting_position))
print(neighbors)

main_tiles = neighbors[:]
while neighbors[0] != neighbors[1]:
    neighbors[0] = neighbors[0].get_next_tile()
    neighbors[1] = neighbors[1].get_next_tile()
    main_tiles += neighbors

print(f"main tiles: {main_tiles}")
main_positions = list(map(lambda x: x.position, main_tiles))
print(f"main positions: {main_positions}")

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c not in [".", "S"] and (row, col) not in main_positions:
            # print(f"trouvé hors main {(row, col)}")
            replace_at_position_by(lines, row, col, ".")

for line in lines:
    line = line.rstrip()
    print(f"{line}")

appended_lines = []
for row, line in enumerate(lines):
    if row:
        appended_lines.append("#" * ((len(line) - 1) * 2 - 1))
    appended_lines.append(("#".join(line))[:-2])

completed_lines = appended_lines[:]
for row, line in enumerate(appended_lines):
    for col, c in enumerate(line):
        # print(f"row {row} col {col}")
        if c in ["J", "-", "7"]:
            # print(f"trouvé {c} at {row}:{col} in {line}, adding - before, to get {completed_lines[row]}")
            replace_at_position_by(completed_lines, row, col - 1, "-")
        if c in ["J", "L", "|"]:
            # print(f"trouvé {c} at {row}:{col} in {line}, adding | before")
            replace_at_position_by(completed_lines, row - 1, col, "|")
        if c in ["F", "-", "L"]:
            # print(f"trouvé {c} at {row}:{col} in {line}, adding - before, to get {completed_lines[row]}")
            replace_at_position_by(completed_lines, row, col + 1, "-")
        if c in ["7", "F", "|"]:
            # print(f"trouvé {c} at {row}:{col} in {line}, adding | before")
            replace_at_position_by(completed_lines, row + 1, col, "|")

for line in completed_lines:
    print(line)

sweeped = []
zones = []

for row, line in enumerate(completed_lines):
    for col, c in enumerate(line):
        if c in ["#", "."] and (row, col) not in sweeped:
            print(f"New tile not swept yet {(row, col)}")
            area_sweeped = []
            area_characters = []
            to_swep = [(row, col)]
            while len(to_swep):
                position = to_swep.pop()
                area_sweeped.append(position)
                area_characters.append(completed_lines[position[0]][position[1]])

                for direction in directions:
                    neighbour_position = (
                        min(len(completed_lines) - 1, max(0, position[0] + direction[0])),
                        min(len(completed_lines[0]) - 1, max(0, position[1] + direction[1]))
                    )
                    # print(f"-- checking {neighbour_position}")
                    if neighbour_position not in area_sweeped \
                            and neighbour_position not in to_swep \
                            and completed_lines[neighbour_position[0]][neighbour_position[1]] in ["#", "."]:
                        to_swep.append(neighbour_position)
                # print(f"- area sweeped {area_sweeped}")
                # print(f"- to_swep {to_swep}")
            print(f"Total area sweeped {area_sweeped}")
            print(f"Total area characters {area_characters}")
            for position in area_sweeped:
                if position[0] in [0, len(completed_lines) - 1] or position[1] in [0, len(completed_lines[0]) - 1]:
                    print(f"Nope, this one is closed {area_sweeped}")
                    for position in area_sweeped:
                        replace_at_position_by(completed_lines, position[0], position[1], "O")
                    break
            else:
                print(f"Hourra, we found an enclosed group {area_sweeped}")
                total += len(list(filter(lambda x: x == ".", area_characters)))
                for position in area_sweeped:
                    if completed_lines[position[0]][position[1]] == ".":
                        replace_at_position_by(completed_lines, position[0], position[1], "I")
            sweeped += area_sweeped

for line in completed_lines:
    print(line)

print(f"Solution {total}")
