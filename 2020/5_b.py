file = open('5.txt', 'r')
Lines = file.readlines()
  
# Strips the newline character
row_size = 64
col_size = 4
max_id = 0
seats = ["{}-{}".format(x, y) for x in range(128) for y in range(8)]
for seat in seats:
    print(seat)
for line in Lines:
    print("{}".format(line.strip()))
    front_back = line[0:7]
    left_right = line[7:]
    #print("{} and {}".format(front_back, left_right))
    row = 0
    for i, letter in enumerate(front_back):
        if letter == "B":
            row += int(row_size / 2**i)
    col = 0
    for i, letter in enumerate(left_right):
        if letter == "R":
            col += int(col_size / 2**i)
    seat = "{}-{}".format(row, col)
    print("removing {}".format(seat))
    if seat in seats:
        seats.remove(seat)
    #max_id = max(max_id, row * 8 + col)

#print("{}".format(max_id))
print("{}".format(seats))
