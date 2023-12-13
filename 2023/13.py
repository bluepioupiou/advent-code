import re
import functools
import itertools
file = open('13.txt', 'r')
lines = file.readlines()

total = 0


def get_pattern_column(pattern, column):
    return "".join([line[column] for line in pattern])


current_pattern = []
for line in lines:
    if line.rstrip() != "":
        current_pattern.append(line.rstrip())
    else:
        print(f"Working with pattern {current_pattern}")
        for row, pattern_line in enumerate(current_pattern[:-1]):
            if pattern_line == current_pattern[row + 1]:
                print(f"Found an horizontal reflexion at {row}, is it through ? ")
                row_before = row - 1
                row_after = row + 2
                while row_before >= 0 and row_after < len(current_pattern):
                    print(f" - Comparing row {current_pattern[row_before]} and {current_pattern[row_after]}")
                    if current_pattern[row_after] != current_pattern[row_before]:
                        break
                    else:
                        row_before -= 1
                        row_after += 1
                else:
                    print(f"Found an horizontal reflexion above {row + 1}")
                    total += 100 * (row + 1)
                    break
        else:
            print(f"No horizontal reflexion in this pattern")
        for col, char in enumerate(current_pattern[0][:-1]):
            if get_pattern_column(current_pattern, col) == get_pattern_column(current_pattern, col + 1):
                print(f"Found a vertical reflexion at {col}, is it through ? ")
                col_before = col - 1
                col_after = col + 2
                while col_before >= 0 and col_after < len(current_pattern[0]):
                    print(f" - Comparing col {get_pattern_column(current_pattern, col_before)} and {get_pattern_column(current_pattern, col_after)}")
                    if get_pattern_column(current_pattern, col_before) != get_pattern_column(current_pattern, col_after):
                        break
                    else:
                        col_before -= 1
                        col_after += 1
                else:
                    print(f"Found a vertical reflexion before {col + 1}")
                    total += col + 1
                    break
        else:
            print(f"No vertical reflexion in this pattern")
        current_pattern = []

print(f"Solution {total}")
