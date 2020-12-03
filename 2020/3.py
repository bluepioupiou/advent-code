file = open('3.txt', 'r')
Lines = file.readlines()
  
# Strips the newline character
tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for right, down in tests:
    trees = 0
    col = 0
    for i, line in enumerate(Lines[down::down]):
        #print("{}".format(line[:-1]), end=' --> ')
        col += right
        if col >= len(line) - 1:
            col -= len(line) - 1
        position = line[col]
        line = list(line)
        line[col] = "X"
        line = "".join(line)
        #print("{}".format(line[:-1]))
        if position == "#":
            trees += 1
    #print("{}".format(trees))
    result *= trees
print("{}".format(result))
