file = open('8.txt', 'r')
Lines = file.readlines()

# Strips the newline character
accumulator = 0
executed = []
row_number = 0
while True:
    if row_number in executed:
        break
    executed.append(row_number)
    line = Lines[row_number]
    instruction, value = line.strip().split(" ")
    if instruction == "nop":
        row_number += 1
    elif instruction == "acc":
        accumulator += int(value)
        row_number += 1
    elif instruction == "jmp":
        row_number += int(value)
    print("encountered {} with {}, going to {}".format(instruction, value, row_number))


print("{}".format(accumulator))
