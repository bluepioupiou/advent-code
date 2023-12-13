

def get_horizontal_reflexion(pattern):
    for row, pattern_line in enumerate(pattern[:-1]):
        if pattern_line == pattern[row + 1]:
            print(f" -- Found an horizontal reflexion at {row}, is it through ? ")
            row_before = row - 1
            row_after = row + 2
            while row_before >= 0 and row_after < len(pattern):
                print(f" --- Comparing row {pattern[row_before]} and {pattern[row_after]}")
                if pattern[row_after] != pattern[row_before]:
                    break
                else:
                    row_before -= 1
                    row_after += 1
            else:
                print(f" -- Found an horizontal reflexion above {row + 1}")
                return 100 * (row + 1)
    return None


def get_vertical_reflexion(pattern):
    for col, char in enumerate(pattern[0][:-1]):
        if get_pattern_column(pattern, col) == get_pattern_column(pattern, col + 1):
            print(f" -- Found a vertical reflexion at {col}, is it through ? ")
            col_before = col - 1
            col_after = col + 2
            while col_before >= 0 and col_after < len(pattern[0]):
                print(
                    f" --- Comparing col {get_pattern_column(pattern, col_before)} and {get_pattern_column(pattern, col_after)}")
                if get_pattern_column(pattern, col_before) != get_pattern_column(pattern, col_after):
                    break
                else:
                    col_before -= 1
                    col_after += 1
            else:
                print(f" -- Found a vertical reflexion before {col + 1}")
                return col + 1


def get_pattern_column(pattern, column):
    return "".join([line[column] for line in pattern])


def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]

if __name__ == '__main__':

    file = open('13.txt', 'r')
    lines = file.readlines()

    total = 0




    current_pattern = []
    for line in lines:
        if line.rstrip() != "":
            current_pattern.append(line.rstrip())
        else:
            print(f"Working with pattern {current_pattern}")
            basic_horizontal_reflexion = get_horizontal_reflexion(current_pattern)
            basic_vertical_reflexion = get_vertical_reflexion(current_pattern)

            for x, l in enumerate(current_pattern):
                for y, c in enumerate(l):
                    modified_pattern = current_pattern[:]
                    new_char = "#"
                    if c == "#":
                        new_char = "."
                    change_in_pattern(modified_pattern, x, y, new_char)
                    print(f" - row {x} col {y} : use modified pattern {modified_pattern}")
                    horizontal_reflexion = get_horizontal_reflexion(modified_pattern)
                    if horizontal_reflexion and horizontal_reflexion != basic_horizontal_reflexion:
                        total += horizontal_reflexion
                        break
                    else:
                        print(f" -> No horizontal reflexion in this pattern")
                        vertical_reflexion = get_vertical_reflexion(modified_pattern)
                        if vertical_reflexion and vertical_reflexion != basic_vertical_reflexion:
                            total += vertical_reflexion
                            break
                        else:
                            print(f" -> No vertical reflexion in this pattern")
                            continue
                else:
                    continue
                break
            current_pattern = []

    print(f"Solution {total}")
