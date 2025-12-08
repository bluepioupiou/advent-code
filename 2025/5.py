from utils import log

if __name__ == '__main__':
    file = open('5.txt', 'r')
    lines = file.readlines()
    result = 0
    ranges = []
    for line in lines:
        line = line.strip()
        if "-" in line:
            left, right = line.split("-")
            ranges.append((int(left), int(right)))
        elif line == "":
            log(ranges)
        else:
            log(f"Analysing {line}")
            for fresh_range in ranges:
                if int(line) in range(fresh_range[0], fresh_range[1] + 1):
                    log(f"{int(line)} in {fresh_range}")
                    result += 1
                    break
    print(result)
