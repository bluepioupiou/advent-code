from utils import log

if __name__ == '__main__':
    file = open('1.txt', 'r')
    lines = file.readlines()

    position = 50
    number_of_zeros = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            distance *= -1

        position += distance
        position = position % 100

        if position == 0:
            number_of_zeros += 1
        log(f"The dial is rotated {line} to point at {position}")

    print(number_of_zeros)
