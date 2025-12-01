from utils import log, Grid, Position, DIRECTIONS
from functools import reduce

file = open('11.txt', 'r')
lines = file.readlines()

if __name__ == '__main__':
    pure_numbers = [int(x) for x in lines[0].split(" ")]
    numbers = {}
    for number in pure_numbers:
        numbers[number] = 1
    log(numbers)
    for blink in range(125):
        new_numbers = {}
        for number, count in numbers.items():
            if number == 0:
                next_numbers = [1]
            elif len(str(number)) % 2 == 0:
                next_numbers = [int(str(number)[:len(str(number))//2]), int(str(number)[len(str(number))//2:])]
            else:
                number *= 2024
                next_numbers = [number]

            for next_number in next_numbers:
                if next_number in new_numbers.keys():
                    new_numbers[next_number] += count
                else:
                    new_numbers[next_number] = count

        numbers = new_numbers
        log(new_numbers)

    print(reduce(lambda a, b: a + b, numbers.values()))