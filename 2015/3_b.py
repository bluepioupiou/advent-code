file = open('3.txt', 'r')
lines = file.readlines()

moves_position = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}
grid = {0: {0: True}}
total = 0


def distribute_in_grid(moves):
    print(moves)
    position = (0, 0)

    for char in moves:
        move = moves_position[char]
        position = (position[0] + move[0], position[1] + move[1])
        if position[0] not in grid:
            grid[position[0]] = {}
        grid[position[0]][position[1]] = True


distribute_in_grid(lines[0][::2])
distribute_in_grid(lines[0][1::2])

for row in grid.values():
    total += len(row)

print(total)
