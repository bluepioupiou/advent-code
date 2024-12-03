file = open('3.txt', 'r')
lines = file.readlines()

total = 0
grid = {0: {0: True}}
position = (0, 0)
moves = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}

for char in lines[0]:
    move = moves[char]
    position = (position[0] + move[0], position[1] + move[1])
    if position[0] not in grid:
        grid[position[0]] = {}
    grid[position[0]][position[1]] = True

for row in grid.values():
    total += len(row)

print(total)
