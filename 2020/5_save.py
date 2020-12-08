file = open('5.txt', 'r')
Lines = file.readlines()
  
# Strips the newline character
row_size = 64
col_size = 4
max_id = 0
rows = range(127)
cols = range(7)
print("{} {}".format(rows, cols))
for line in Lines:
    remaining_rows = list(rows)
    remaining_cols = list(cols)
    front_back = line[0:7]
    left_right = line[7:]
    print("{} {}".format(front_back, left_right))

    #print("{} and {}".format(front_back, left_right))
    row = 0
    for letter in front_back:
        if letter == "F":
            remaining_rows = remaining_rows[:len(remaining_rows)//2]
        else:
            remaining_rows = remaining_rows[len(remaining_rows) // 2+1:]
        print("rows {}".format(remaining_rows))

    for letter in left_right:
        if letter == "L":
            remaining_cols = remaining_cols[:len(remaining_cols)//2]
        else:
            remaining_cols = remaining_cols[len(remaining_cols) // 2+1:]
        print("cols {}".format(remaining_cols))

    print("row {} col {}".format(remaining_rows, remaining_cols))
print(list(remaining_rows)[0] * 8 + list(remaining_cols)[0])

