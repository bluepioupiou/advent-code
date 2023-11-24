
file = open('10.txt', 'r')
lines = file.read().splitlines()
X = 1
cycle = 1
row = ""


def resolve_sprite(row, cycle, X):
    position = cycle % 40 - 1
    # print("During cycle {}: CRT draw pixel in position {}".format(cycle, position))
    if abs(position - X) <= 1:
        row += "#"
    else:
        row += "."
    if cycle % 40 == 0:
        print(row)
        row = ""
    # print("Current CRT row: {}".format(row))
    return row


for line in lines:
    if line == "noop":
        row = resolve_sprite(row, cycle, X)
        cycle += 1
    else:
        command, number = line.split(" ")
        # print("Start cycle {}: executing {} {}".format(cycle, command, number))
        row = resolve_sprite(row, cycle, X)
        cycle += 1
        row = resolve_sprite(row, cycle, X)
        cycle += 1
        X += int(number)
        # print("End of cycle {}: finish executing {} {}".format(cycle, command, number))
        # print("Sprint position : {}".format(X))
