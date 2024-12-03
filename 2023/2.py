file = open('2.txt', 'r')
lines = file.readlines()
maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0
for game_id, line in enumerate(lines, 1):
    print(game_id)
    sets = line.split(": ")[-1].split("; ")
    good_game = True
    for set in sets:
        print("- set:", set)
        cubes = set.split(", ")
        for cube in cubes:
            print("-- cube:", cube)
            number = int(cube.split(" ")[0])
            color = cube.split(" ")[1].rstrip()
            print("---", number, "-", color)
            if number > maxes[color]:
                good_game = False
                break
    if good_game:
        total += game_id
print(total)
