file = open('13.txt', 'r')
Lines = file.readlines()

time = 0
buses = Lines[1].split(",")
first = int(buses[0])
print(buses)
while True:
    time += 1
    for num, bus in enumerate(buses):
        try:
            if (first * time + num) % int(bus):
                break
        except ValueError:
            pass
    else:
        break

print("{}".format(time * first))
