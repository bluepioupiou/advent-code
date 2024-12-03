from functools import reduce

file = open('2.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    dimensions = [int(x) for x in line.split("x")]
    dimensions.sort()
    total += 2 * dimensions[0] + 2 * dimensions[1] + reduce(lambda x, y: x * y, dimensions)
print(total)
