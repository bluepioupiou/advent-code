file = open('2.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    levels = [int(x) for x in line.replace("\n", "").split(" ")]
    direction = None
    for levelX, levelY in zip(levels[::], levels[1::]):
        if not 1 <= abs(levelX - levelY) <= 3:
            break
        if direction is None:
            direction = "decrease" if levelX > levelY else "increase"
        else:
            new_direction = "decrease" if levelX > levelY else "increase"
            if new_direction != direction:
                break
    else:
        total += 1

print(total)
