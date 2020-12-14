file = open('13.txt', 'r')
Lines = file.readlines()

start = int(Lines[0])
buses = Lines[1].split(",")
buses = list(filter(lambda x: x != "x", buses))
best = 999
best_bus = None
print(buses)
print("{} {}".format("time\t", "\t".join(buses)))

for time in range(start-20, start+20):
    print("{} {}".format(time, "\t".join(["D" if time % int(bus) == 0 else "." for bus in buses])))

for bus in buses:
    bus = int(bus)
    print("Reste de {} modulo {} = {}".format(start, bus, (bus - start % bus) % bus))
    wait = (bus - start % bus) % bus
    if wait < best:
        best = (bus - start % bus) % bus
        best_bus = bus

print("{}".format(best * best_bus))
