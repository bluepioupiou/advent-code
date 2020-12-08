file = open('8.txt', 'r')
Lines = file.readlines()

# Strips the newline character
terminated = False
for changed in range(len(Lines)):
    accumulator = 0
    executed = []
    row_number = 0

    print("trying to change line {}".format(changed))
    while True:
        if row_number in executed:
            break
        if row_number == len(Lines):
            terminated = True
            break
        executed.append(row_number)
        line = Lines[row_number]
        instruction, value = line.strip().split(" ")
        if instruction == "nop" or (instruction == "jmp" and row_number == changed):
            row_number += 1
        elif instruction == "acc":
            accumulator += int(value)
            row_number += 1
        elif instruction == "jmp" or (instruction == "nop" and row_number == changed):
            row_number += int(value)
        print("encountered {} with {}, going to {}".format(instruction, value, row_number))
    if terminated:
        break



print("{}".format(accumulator))
