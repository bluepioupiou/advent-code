file = open('1.txt', 'r')
lines = file.readlines()

floor = 0
line = lines[0]
for char in line:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
print(floor)
