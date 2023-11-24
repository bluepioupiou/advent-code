file = open('1.txt', 'r')
lines = file.readlines()

total = 0
previous_depth = None
for number in range(1, len(lines)-1):
    one = int(lines[number-1])
    two = int(lines[number])
    three = int(lines[number+1])
    depth = one + two + three
    if previous_depth and previous_depth < depth:
        total += 1
    previous_depth = depth
print(total)
