file = open('10.txt', 'r')
Lines = file.readlines()

# Strips the newline character
jolts = [int(x) for x in Lines]
jolts.sort()
jolts.append(jolts[-1]+3)
print("{}".format(jolts))
previous = 0
one_gap = 0
total = 1
for jolt in jolts:
    if jolt - previous == 1:
        one_gap += 1
        print("found jolt {}, onegap = {}".format(jolt, one_gap))
    else:
        print("found jolt {}, breaking and multiplying by {}".format(jolt, ((2 ** max(0, (one_gap - 1))) - max(0, one_gap - 3))))

        total = total * ((2 ** max(0, (one_gap - 1))) - max(0, one_gap - 3))
        one_gap = 0
    previous = jolt

print("{}".format(total))
