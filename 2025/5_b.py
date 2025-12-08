from utils import log

if __name__ == '__main__':
    file = open('5.txt', 'r')
    lines = file.readlines()
    result = 0
    ranges = [[int(x[0]), int(x[1])] for x in [line.strip().split("-") for line in lines]]

    ranges = sorted(ranges, key=lambda x: x[0])
    while ranges:
        log(ranges)
        first = ranges.pop(0)
        second = ranges[0]
        if second[0] <= first[1]:
            new = [first[0], max(first[1], second[1])]
            ranges.pop(0)
            ranges.insert(0, new)
            break
        else:
            result += first[1] - first[0] + 1


    print(result)
