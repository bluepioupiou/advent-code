import re
file = open('3.txt', 'r')
lines = file.readlines()

total = 0
programm = ""
for line in lines:
    programm += line
while "don't()" in programm:
    dont_position = programm.index("don't()")
    if "do()" in programm[dont_position:]:
        do_position = programm.index("do()", dont_position)
        programm = programm[:dont_position] + programm[do_position:]
    else:
        programm = programm[:dont_position]

#print(line)
matchs = re.findall("mul\((\d*),(\d*)\)", programm)
print(matchs)
for number1, number2 in matchs:
    total += int(number1) * int(number2)

print(total)
