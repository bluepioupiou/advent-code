file = open('4.txt', 'r')
lines = file.read().splitlines()

total = 0
for line in lines:
    first, second = line.split(",")
    first_start, first_stop = [int(x) for x in first.split("-")]
    second_start, second_stop = [int(x) for x in second.split("-")]
    print("{}-{},{}-{}".format(first_start, first_stop, second_start, second_stop))
    if not (first_stop < second_start or first_start > second_stop):
        total += 1

print(total)
