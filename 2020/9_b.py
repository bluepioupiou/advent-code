file = open('9.txt', 'r')
Lines = file.readlines()

# Strips the newline character
preamble = 25
analyzed_line = preamble
for line in Lines[preamble:]:
    inspected_sum = int(line)
    for x in Lines[analyzed_line - preamble:analyzed_line]:
        for y in Lines[analyzed_line - preamble:analyzed_line]:
            if int(x) + int(y) == inspected_sum and x != y:
                break
        else:
            continue
        break
    else:
        break
    analyzed_line += 1

print("{}".format(inspected_sum))

for start in range(len(Lines)):
    contiguous_sum = 0
    numbers = []
    for line in Lines[start:]:
        contiguous_sum += int(line)
        numbers.append(int(line))
        if contiguous_sum >= inspected_sum:
            break
    if contiguous_sum == inspected_sum:
        solution = max(numbers) + min(numbers)
        break

print("{}".format(solution))
