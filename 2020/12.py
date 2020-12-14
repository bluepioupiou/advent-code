import itertools
file = open('12.txt', 'r')
Lines = file.readlines()

directions = ["N", "E", "S", "W"]
actual_direction = "E"

latitude = 0
longitude = 0

for line in Lines:
    action = line[0]
    value = line[1:-1]

    if action == "F":
        action = actual_direction

    print("going {} for {}".format(action, value))

    if action == "N":
        latitude += int(value)
    elif action == "S":
        latitude -= int(value)
    elif action == "E":
        longitude += int(value)
    elif action == "W":
        longitude -= int(value)
    elif action == "R" or action == "L":
        actual_position = directions.index(actual_direction)
        diff = int(int(value)/90)
        if action == "R":
            new_position = actual_position + diff
        else:
            new_position = actual_position - diff
        actual_direction = directions[new_position % 4]
        print("new direction {}".format(actual_direction))

    print("{} {}".format(longitude, latitude))

print("{}".format(abs(longitude) + abs(latitude)))
