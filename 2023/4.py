import re
file = open('4.txt', 'r')
lines = file.readlines()


total = 0
for line in lines:
    all = line.split(":")[1]
    winnings = re.findall('\d+', all.split("|")[0])
    numbers = re.findall('\d+', all.split("|")[1])
    print(winnings, numbers)
    intersection = set(winnings).intersection(set(numbers))
    print(len(intersection))
    if len(intersection):
        total += 2 ** (len(intersection) - 1)
print(total)
