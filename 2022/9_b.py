file = open('9.txt', 'r')
lines = file.read().splitlines()


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}
rows = 25
cols = 25
start = (20, 12)
rope = []
tail_positions = []
for i in range(0, 11):
    rope.append((start[0], start[1]))


def display_grid():
    for row in range(0, rows):
        output = ""
        for col in range(0, cols):
            for count, current_knot in enumerate(rope):
                if row == current_knot[0] and col == current_knot[1]:
                    if count == 0:
                        output += "H"
                    else:
                        output += str(count)
                    break
            else:
                output += "."
        print(output)
    print("")


display_grid()
for line in lines:
    print("Applying {}".format(line))
    direction, steps = line.split()
    for i in range(0, int(steps)):
        change = directions[direction]
        for knot in range(0, len(rope) - 1):
            head = rope[knot]
            tail = rope[knot + 1]

            head = (head[0] + change[0], head[1] + change[1])
            rope[knot] = head
            #print("new head {}".format(head))
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
            print("new rope head {}".format(rope[0]))

        tail_positions.append(tail)
    display_grid()

tail_positions = list(set(tail_positions))
print("result {}".format(len(tail_positions)))
