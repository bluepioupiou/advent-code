file = open('2.txt', 'r')
lines = file.readlines()

total = 0
for game_id, line in enumerate(lines, 1):
    print(line)
    sets = line.split(": ")[-1].split("; ")
    good_game = True
    maxes = {
        'red': None,
        'green': None,
        'blue': None
    }
    for set in sets:
        print("- set:", set)
        cubes = set.split(", ")
        for cube in cubes:
            print("-- cube:", cube)
            number = int(cube.split(" ")[0])
            color = cube.split(" ")[1].rstrip()
            print("---", number, "-", color)
            if not maxes[color] or number > maxes[color]:
                maxes[color] = number
    print("---->", maxes)
    power = 1
    for number in maxes.values():
        power *= number
    print(power)
    total += power
print(total)
