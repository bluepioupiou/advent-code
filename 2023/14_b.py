import re
import functools
import itertools


def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]


def move_north(pattern):
    for row, line in enumerate(pattern):
        pattern[row] = line.strip()
        for col, char in enumerate(line):
            # print(f" - Annalysing {row}/{col}")
            if char == "O":
                new_row = row
                while new_row > 0 and pattern[new_row - 1][col] == ".":
                    new_row -= 1
                # print(f" - found O at {row}/{col} new row to slide {new_row}")
                change_in_pattern(pattern, row, col, ".")
                change_in_pattern(pattern, new_row, col, "O")


def move_west(pattern):
    for row, line in enumerate(pattern):
        pattern[row] = line.strip()
        for col, char in enumerate(line):
            # print(f" - Annalysing {row}/{col}")
            if char == "O":
                new_col = col
                while new_col > 0 and pattern[row][new_col - 1] == ".":
                    new_col -= 1
                # print(f" - found O at {row}/{col} new row to slide {new_row}")
                change_in_pattern(pattern, row, col, ".")
                change_in_pattern(pattern, row, new_col, "O")


def calculate_weight(pattern):
    total = 0
    for row, line in enumerate(pattern):
        total += line.count("O") * (len(pattern) - row)
    return total


def display_pattern(pattern):
    for line in pattern:
        print(line)


def do_cycle(pattern):
    # North
    move_north(pattern)
    # print("After North")
    # display_pattern(lines)

    # West
    move_west(pattern)
    # print("After West")
    # display_pattern(lines)

    # South
    pattern.reverse()
    move_north(pattern)
    pattern.reverse()
    # print("After South")
    # display_pattern(lines)

    # East
    for row, line in enumerate(pattern):
        pattern[row] = line[::-1]
    move_west(pattern)
    for row, line in enumerate(pattern):
        pattern[row] = line[::-1]
    # print("After East")


if __name__ == '__main__':
    file = open('14.txt', 'r')
    lines = file.readlines()

    for i in range(1, 1000):
        do_cycle(lines)

        total = calculate_weight(lines)
        #print(f"iter {i} total {total}")
        #display_pattern(lines)

    stabilized = False
    suite = [calculate_weight(lines)]
    new_suite = []
    print(f"Trying to find suite")
    while not stabilized:
        i =+ 1
        do_cycle(lines)
        new_suite.append(calculate_weight(lines))
        if new_suite == suite[:len(new_suite)] and len(suite) > 3:
            print(f"Finding {new_suite} into {suite}")
            if new_suite == suite:
                print(f"Found suite : {suite}")
                break
            continue
        else:
            suite += new_suite
            new_suite = []
        print(f"suite {suite}")

    result = suite[(1000000000 - i) % len(suite)]
    print(result)
