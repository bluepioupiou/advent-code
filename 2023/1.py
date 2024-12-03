file = open('1.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    only_decimals = [c for c in line if c.isdecimal()]
    number = int(f"{only_decimals[0]}{only_decimals[-1]}")
    total += number
print(total)
