file = open('2.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    levels = [int(x) for x in line.replace("\n", "").split(" ")]
    one_safe = False
    for index in range(len(levels)):
        new_levels = list(levels)
        del new_levels[index]
        direction = None
        for levelX, levelY in zip(new_levels[::], new_levels[1::]):
            if not 1 <= abs(levelX - levelY) <= 3:
                break
            if direction is None:
                direction = "decrease" if levelX > levelY else "increase"
            else:
                new_direction = "decrease" if levelX > levelY else "increase"
                if new_direction != direction:
                    break
        else:
            one_safe = True
    if one_safe:
        total += 1
print(total)
