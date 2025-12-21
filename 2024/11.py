from utils import log, Grid, Position, DIRECTIONS

file = open('11.txt', 'r')
lines = file.readlines()

if __name__ == '__main__':
    numbers = [int(x) for x in lines[0].split(" ")]
    log(numbers)
    for blink in range(75):
        new_numbers = []
        for number in numbers:
            if number == 0:
                new_numbers.append(1)
            elif len(str(number)) % 2 == 0:
                new_numbers += [int(str(number)[:len(str(number))//2]), int(str(number)[len(str(number))//2:])]
            else:
                number *= 2024
                new_numbers.append(number)
        log(new_numbers)
        numbers = new_numbers
    print(len(numbers))