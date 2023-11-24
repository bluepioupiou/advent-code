file = open('4.txt', 'r')
lines = file.read().splitlines()

total = 0
for line in lines:
    first, second = line.split(",")
    first_start, first_stop = [int(x) for x in first.split("-")]
    second_start, second_stop = [int(x) for x in second.split("-")]
    print("{}-{},{}-{}".format(first_start, first_stop, second_start, second_stop))
    print("{};{};{};{}".format(first_start <= second_start, second_stop <= first_stop, second_start <= first_start, first_stop <= second_stop))
    if (first_start <= second_start and second_stop <= first_stop) or (second_start <= first_start and first_stop <= second_stop):
        print("- true comparison")
        total += 1

print(total)
