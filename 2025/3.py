from utils import log

if __name__ == '__main__':
    file = open('3.txt', 'r')
    lines = file.readlines()
    result = 0

    for line in lines:
        max_joltage = 0
        for num, first in enumerate(line[:-1]):
            for second in line[num+1:-1]:
                #log(f"Trying {first} with {second}")
                joltage = int(f"{first}{second}")
                max_joltage = max(max_joltage, joltage)
        result += max_joltage

    print(result)
