from utils import Grid, Position, DIRECTIONS

file = open('7.txt', 'r')
lines = file.readlines()

total = 0

if __name__ == '__main__':
    for line in lines:
        test_value, numbers = line.split(": ")
        possibilities = []
        for number in [int(x) for x in numbers.split(" ")]:
            if not possibilities:
                possibilities.append(number)
            else:
                new_possibilities = []
                for possibility in possibilities:
                    new_possibilities.append(possibility + number)
                    new_possibilities.append(possibility * number)
                possibilities = new_possibilities
        print(f"For test valie {test_value}, possibilities = {possibilities}")
        if int(test_value) in possibilities:
            total += int(test_value)
    print(total)

