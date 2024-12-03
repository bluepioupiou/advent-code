import re
file = open('3.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    matchs = re.findall("mul\((\d*),(\d*)\)", line)
    for number1, number2 in matchs:
        total += int(number1) * int(number2)

print(total)

line = re.sub("(don't\(\).*?do\(\))", "", line)
if "don't()" in line:
    line = line[:line.index("don't()")]
print(line)
matchs = re.findall("mul\((\d*),(\d*)\)", line)
for number1, number2 in matchs:
    total += int(number1) * int(number2)