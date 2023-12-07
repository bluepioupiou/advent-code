import re
file = open('6.txt', 'r')
lines = file.readlines()

times = [int(x) for x in re.findall('\d+', lines[0].split(":")[1])]
distances = [int(x) for x in re.findall('\d+', lines[1].split(":")[1])]

total = 1
for race_number, time in enumerate(times):
    winnings = 0
    for pressed in range(time):
        distance = pressed * (time - pressed)
        if distance > distances[race_number]:
            winnings += 1
    total *= winnings
print(f"Solution {total}")
