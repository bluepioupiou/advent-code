file = open('9.txt', 'r')
lines = file.read().splitlines()


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}
rows = 5
cols = 6
head = (4, 0)
tail = (4, 0)
tail_positions = []

def display_grid(head, tail):
    for row in range(0, rows):
        output = ""
        for col in range(0, cols):
            if row == head[0] and col == head[1]:
                output += "H"
            elif row == tail[0] and col == tail[1]:
                output += "T"
            else:
                output += "."
        print(output)
    print("")


for line in lines:
    print("Applying {}".format(line))
    direction, steps = line.split()
    for i in range(0, int(steps)):
        change = directions[direction]
        head = (head[0] + change[0], head[1] + change[1])
        diff_V = abs(tail[0] - head[0])
        diff_H = abs(tail[1] - head[1])
        new_V, new_H = tail
        if diff_V == 2:
            new_V = (tail[0] + head[0]) // 2
            if diff_H == 1:
                new_H = head[1]
        elif diff_H == 2:
            new_H = (tail[1] + head[1]) // 2
            if diff_V == 1:
                new_V = head[0]
        tail = (new_V, new_H)
        tail_positions.append(tail)
        display_grid(head, tail)

tail_positions = list(set(tail_positions))
print("result {}".format(len(tail_positions)))
