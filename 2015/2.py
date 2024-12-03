file = open('2.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    l, w, h = [int(x) for x in line.split("x")]
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h ,h*l)
print(total)
