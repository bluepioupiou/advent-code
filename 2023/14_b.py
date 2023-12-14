import re
import functools
import itertools
file = open('14.txt', 'r')
lines = file.readlines()


def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]


if __name__ == '__main__':
    for i in range(3):
        total = 0

        # North
        for row, line in enumerate(lines):
            lines[row] = line.strip()
            for col, char in enumerate(line):
                #print(f" - Annalysing {row}/{col}")
                if char == "O":
                    new_row = row
                    while new_row > 0 and lines[new_row - 1][col] == ".":
                        new_row -= 1
                    #print(f" - found O at {row}/{col} new row to slide {new_row}")
                    change_in_pattern(lines, row, col, ".")
                    change_in_pattern(lines, new_row, col, "O")
        print("After North")
        for row, line in enumerate(lines):
            print(line)
        # West
        for row, line in enumerate(lines):
            lines[row] = line.strip()
            for col, char in enumerate(line):
                # print(f" - Annalysing {row}/{col}")
                if char == "O":
                    new_col = col
                    while new_col > 0 and lines[row][new_col - 1] == ".":
                        new_col -= 1
                    # print(f" - found O at {row}/{col} new row to slide {new_row}")
                    change_in_pattern(lines, row, col, ".")
                    change_in_pattern(lines, row, new_col, "O")

        print("After West")
        for row, line in enumerate(lines):
            print(line)

        # South
        for row, line in enumerate(lines):
            lines[row] = line.strip()
            for col, char in enumerate(line):
                # print(f" - Annalysing {row}/{col}")
                if char == "O":
                    new_row = row
                    while new_row < len(lines) -1  and lines[new_row + 1][col] == ".":
                        new_row += 1
                    # print(f" - found O at {row}/{col} new row to slide {new_row}")
                    change_in_pattern(lines, row, col, ".")
                    change_in_pattern(lines, new_row, col, "O")

        print("After South")
        for row, line in enumerate(lines):
            print(line)

        # East
        for row, line in enumerate(lines):
            lines[row] = line.strip()
            for col, char in enumerate(line):
                # print(f" - Annalysing {row}/{col}")
                if char == "O":
                    new_col = col
                    while new_col < len(line) - 1 and lines[row][new_col + 1] == ".":
                        new_col += 1
                    # print(f" - found O at {row}/{col} new row to slide {new_row}")
                    change_in_pattern(lines, row, col, ".")
                    change_in_pattern(lines, row, new_col, "O")

        print("After East")
        for row, line in enumerate(lines):
            print(line)
            total += line.count("O") * (len(lines) - row)

        print(f"After {i} : {total}")
