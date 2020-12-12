import itertools
file = open('11.txt', 'r')
Lines = file.readlines()

# Strips the newline character
seats = [[seat for seat in line.strip()] for line in Lines]
print("from \n{}".format("\n".join(["".join(row) for row in seats])))
while True:
    result = []
    for i, row in enumerate(seats):
        new_row = []
        for j, seat in enumerate(row):
            occupied = 0
            #print("inspecting neighbors for cell {}-{}:{}".format(i, j, seat))
            for x, y in list(itertools.product(range(-1, 2), range(-1, 2))):
                if x != 0 or y != 0:
                    if 0 <= (i + x) < len(seats) and 0 <= (j + y) < len(row):
                        #print("-- neighbor {}/{}:{}".format(i + x, j + y, seats[i + x][j + y]))
                        neighbour = seats[i+x][j+y]
                        if neighbour == "#":
                            occupied += 1
            if seat == "#" and occupied >= 4:
                new_row.append("L")
            elif seat == "L" and occupied == 0:
                new_row.append("#")
            else:
                new_row.append(seat)

        result.append(new_row)

    #print("from \n{}".format("\n".join(["".join(row) for row in seats])))
    print("to \n{}".format("\n".join(["".join(row) for row in result])))
    if "".join(["".join(row) for row in result]) == "".join(["".join(row) for row in seats]):
        break
    else:
        seats = result
print("found {}".format(sum([row.count("#") for row in result])))
