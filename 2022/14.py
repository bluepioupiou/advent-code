file = open('14.txt', 'r')
lines = file.read().splitlines()


def print_paths(paths):
    min_x = min([path[0] for path in paths])
    max_x = max([path[0] for path in paths])
    min_y = min([path[1] for path in paths])
    max_y = max([path[1] for path in paths])
    print(" == Path == ")
    for y in range(min_y - 1, max_y + 2):
        row = ""
        for x in range(min_x - 1, max_x + 2):
            row += paths[(x, y)] if (x, y) in paths else "."
        print(row)


paths = {}
result = 0
below_y = 0
for line in lines:
    corners = line.split(" -> ")
    for i in range(len(corners) - 1):
        start = corners[i]
        end = corners[i + 1]
        print("from {} to {}".format(start, end))
        start_x, start_y = [int(pos) for pos in start.split(",")]
        end_x, end_y = [int(pos) for pos in end.split(",")]
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                below_y = max(y, below_y)
                paths[(x, y)] = "#"

print(below_y)
print_paths(paths)
source = (500, 0)
moving_sand = source

while True:
    down = (moving_sand[0], moving_sand[1] + 1)
    down_left = (moving_sand[0] - 1, moving_sand[1] + 1)
    down_right = (moving_sand[0] + 1, moving_sand[1] + 1)
    if down[1] > below_y:
        print("VOID !!")
        break
    elif down not in paths:
        moving_sand = down
    elif down_left not in paths:
        moving_sand = down_left
    elif down_right not in paths:
        moving_sand = down_right
    else:
        paths[moving_sand] = "O"
        result += 1
        moving_sand = source
        print_paths(paths)

print("Résultat : {}".format(result))
