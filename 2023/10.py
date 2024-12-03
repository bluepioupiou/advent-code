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
        print(self)
        origin_direction = (self.origin[0] - self.position[0], self.origin[1] - self.position[1])
        next_tile_direction = next(filter(lambda x: x != origin_direction, self.pipe.connections))
        print(next_tile_direction)
        next_tile_position = (self.position[0] + next_tile_direction[0], self.position[1] + next_tile_direction[1])
        print(next_tile_position)
        next_tile_type = lines[next_tile_position[0]][next_tile_position[1]]
        print(next_tile_type)
        next_tile_pipe = next(filter(lambda x: x.type == next_tile_type, pipes))
        return Tile(next_tile_pipe, next_tile_position, self.position)


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
        neighbors.append(Tile(pipe, neighbour_position, starting_position))
print(neighbors)

total = 1

while neighbors[0] != neighbors[1]:
    total += 1
    print(f"Distance {total}")
    neighbors[0] = neighbors[0].get_next_tile()
    neighbors[1] = neighbors[1].get_next_tile()
    print(f" - {neighbors[0]}")
    print(f" - {neighbors[1]}")
print(f"Solution {total}")
