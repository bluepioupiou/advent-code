file = open('3.txt', 'r')
lines = file.readlines()


total = 0
already_parsed = False
for row_number, line in enumerate(lines):
    for col_number, digit in enumerate(line):
        if str(digit).isnumeric() and not already_parsed:
            print(f"testing {digit} in {row_number}-{col_number}")
            for row in range(max(0, row_number - 1), min(len(lines), row_number + 2)):
                for col in range(max(0, col_number - 1), min(len(lines), col_number + 2)):
                    print(f" - {row} {col}")
                    if lines[row][col] != "." and not lines[row][col].isnumeric():
                        character = lines[row][col]
                        while col_number > 0 and lines[row_number][col_number-1].isnumeric():
                            col_number -= 1
                        start_col = int(col_number)
                        while col_number < len(line)-1 and lines[row_number][col_number+1].isnumeric():
                            col_number += 1
                        col_number += 1
                        end_col = int(col_number)
                        print(f"number {lines[row_number][start_col:end_col]} in {row_number} from {start_col} to {end_col} adjacent to {character}")
                        already_parsed = True
                        total += int(lines[row_number][start_col:end_col])
                        break
                else:
                    continue
                break
        elif not str(digit).isnumeric():
            already_parsed = False
print(total)
