from utils import log

if __name__ == '__main__':
    file = open('2.txt', 'r')
    line = file.readline()
    #log(f"line {line}")

    result = 0
    for ranges in line.split(","):
        start, end = ranges.split("-")
        #log(f"range {ranges} : {start} - {end}")
        for number in range(int(start), int(end) + 1):
            ID = str(number)
            #log(f" {ID}")
            max_sequence_size = len(ID) // 2
            for sequence_size in range(1, max_sequence_size + 1):
                if len(ID) // sequence_size * sequence_size < len(ID):
                    continue
                parts = list(map(''.join, zip(*[iter(ID)] * sequence_size)))
                #log(f" - {parts}")
                if parts.count(parts[0]) == len(parts):
                    #log(f" - found {number}")
                    result += int(number)
                    break
    print(result)
