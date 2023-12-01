file = open('1.txt', 'r')
lines = file.readlines()
words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
total = 0
for line in lines:
    print(line)
    for i in range(len(line)):
        for word, digit in words.items():
            if line[i::].startswith(word):
                line = line.replace(word, digit)
    print(line)
    only_decimals = [c for c in line if c.isdecimal()]
    number = int(f"{only_decimals[0]}{only_decimals[-1]}")
    print(number)
    total += number
print(total)
