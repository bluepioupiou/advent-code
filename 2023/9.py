import re
import functools
file = open('9.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    values = [int(x) for x in re.findall('-?\d+', line)]
    sequences = [values]
    while values and len(list(filter(lambda x: x != 0, values))):
        print(values)
        new_values = []
        for step_x, step_y in zip(values[0:-1], values[1:]):
            #print(step_x, step_y)
            new_values.append(step_y - step_x)
        values = new_values
        if len(values):
            sequences.append(values)

    extrapolate = 0
    for sequence in list(reversed(sequences)):
        extrapolate += sequence[-1]
    print(f"Extrapolate: {extrapolate}")
    total += extrapolate

print(f"Solution {total}")
