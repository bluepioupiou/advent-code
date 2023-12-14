import re
import functools
import itertools
file = open('14.txt', 'r')
lines = file.readlines()

total = 0

def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]

if __name__ == '__main__':
    for row, line in enumerate(lines):
        lines[row] = line.strip()
        for col, char in enumerate(line):
            print(f" - Annalysing {row}/{col}")
            if char == "O":
                new_row = row
                while new_row > 0 and lines[new_row - 1][col] == ".":
                    new_row -= 1
                print(f" - found O at {row}/{col} new row to slide {new_row}")
                change_in_pattern(lines, row, col, ".")
                change_in_pattern(lines, new_row, col, "O")

    for row, line in enumerate(lines):
        print(line)
        total += line.count("O") * (len(lines) - row)

    print(f"Solution {total}")
