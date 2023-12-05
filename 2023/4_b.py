import re
file = open('4.txt', 'r')
lines = file.readlines()
copies = {}
total = 0
for card, line in enumerate(lines, 1):
    all = line.split(":")[1]
    winnings = re.findall('\d+', all.split("|")[0])
    numbers = re.findall('\d+', all.split("|")[1])
    print(winnings, numbers)
    intersections = len(set(winnings).intersection(set(numbers)))
    print(intersections)
    if card not in copies:
        copies[card] = 0
    copies[card] += 1
    for next in range(card + 1, card + intersections + 1):
        print(f"Adding {copies[card]} to {next}")
        if next not in copies:
            copies[next] = 0
        copies[next] += copies[card]
    print(f"copies after {card} : {copies}")
print(copies)
print(sum(v for v in copies.values()))
