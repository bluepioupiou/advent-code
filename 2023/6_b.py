import re
file = open('6.txt', 'r')
lines = file.readlines()

times = re.findall('\d+', lines[0].split(":")[1])
distances = re.findall('\d+', lines[1].split(":")[1])

time = int("".join(times))
record_distance = int("".join(distances))
winnings = 0
for pressed in range(time):
    distance = pressed * (time - pressed)
    if distance > record_distance:
        winnings += 1
print(f"Solution {winnings}")
