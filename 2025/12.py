import re
from utils import log

if __name__ == '__main__':
    file = open('12.txt', 'r')
    result = 0

    shapes = {}
    shape_id = None
    for line in file.readlines():
        if line.strip().endswith(":"):
            shape_id = int(line.split(":")[0])
            shapes[shape_id] = 0
        elif "#" in line:
            shapes[shape_id] += line.count("#")
        elif "x" in line:
            dimensions, counts = line.split(":")
            width, height = map(int, dimensions.split("x"))
            counts = map(int, counts.strip().split(" "))
            if width * height >= sum(count * shapes[i] for i, count in enumerate(counts)):
                result += 1

    print(result)

