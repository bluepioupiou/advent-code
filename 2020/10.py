file = open('10.txt', 'r')
Lines = file.readlines()

# Strips the newline character
jolts = [int(x) for x in Lines]
jolts.sort()
jolts.append(jolts[-1]+3)
print("{}".format(jolts))
previous = 0
one_gap = 0
three_gap = 0
for jolt in jolts:
    if jolt - previous == 1:
        one_gap += 1
    else:
        three_gap += 1
    previous = jolt
print("{} on gap and {} three gap".format(one_gap,three_gap))
print("{}".format(one_gap * three_gap))
