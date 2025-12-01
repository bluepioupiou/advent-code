from utils import log
import math

if __name__ == '__main__':
    file = open('1.txt', 'r')
    lines = file.readlines()

    position = 50
    total_number_of_zeros = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        number_of_zeros = 0

        if direction == "L":
            distance *= -1
        previous_position = position
        position += distance

        # Si ils n'ont pas le meme signe c'est qu'est passé par 0
        if previous_position * position < 0:
            number_of_zeros += 1
        # On rajoute le nombre de fois on est passé par 0
        number_of_zeros += abs(position) // 100
        if position == 0:
            number_of_zeros += 1

        position = position % 100

        log(f"The dial is rotated {line} to point at {position} (and pass to zero {number_of_zeros} times)")
        total_number_of_zeros += number_of_zeros
    print(total_number_of_zeros)
