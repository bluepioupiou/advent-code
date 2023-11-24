file = open('15.txt', 'r')
lines = file.read().splitlines()

row = 2000000
overlaps = {}
for line in lines:
    text1, text2 = line.split(":")
    text1_left, text1_right = text1.split(",")
    text2_left, text2_right = text2.split(",")
    sensor_x = int(text1_left.split("=")[1])
    sensor_y = int(text1_right.split("=")[1])
    beacon_x = int(text2_left.split("=")[1])
    beacon_y = int(text2_right.split("=")[1])
    if beacon_y == row:
        overlaps[beacon_x] = "B"
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    print("found sensor {} {} and beacon {} {} : distance {}".format(sensor_x, sensor_y, beacon_x, beacon_y, distance))
    overlap = distance - abs(row - sensor_y)
    if overlap >= 0:
        print("sensor crossing row at overlap {}".format(overlap))
        for crossing in range(0, overlap + 1):
            if sensor_x + crossing not in overlaps:
                overlaps[sensor_x + crossing] = "#"
            if sensor_x - crossing not in overlaps:
                overlaps[sensor_x - crossing] = "#"
#print(overlaps)
print(len({k: v for k, v in overlaps.items() if v == "#"}))
