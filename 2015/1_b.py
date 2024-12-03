file = open('1.txt', 'r')
lines = file.readlines()

floor = 0
line = lines[0]
for index, char in enumerate(line, 1):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor == -1:
        first = index
        break
print(index)
