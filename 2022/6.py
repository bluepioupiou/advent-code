import re
file = open('6.txt', 'r')
lines = file.read().splitlines()

chars = []
for index, char in enumerate(lines[0]):
    print(char)
    chars.append(char)
    print(chars)
    if len(chars) > 4:
        chars.pop(0)
        distinct_chars = list(set(chars))
        if len(distinct_chars) == len(chars):
            break
    print(chars)

print(index+1)
