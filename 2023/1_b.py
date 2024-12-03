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
    first = None
    current = None
    last = None
    #print(line)
    for i in range(len(line)):
        for word, digit in words.items():
            if line[i::].startswith(word):
                #print(f"---found word {word}")
                current = words[word]
                break
        else:
            if line[i].isdecimal():
                #print(f"---found digit {line[i]}")
                current = line[i]
        if current and not first:
            first = current
        if current:
            last = str(current)
        current = None
        #print(f"{first}-{current}-{last}")

    number = f"{first}{last}"
    print(number)
    total += int(number)
print(total)
