file = open('3.txt', 'r')
lines = file.readlines()

alfa = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define reverse lookup dict
rdict = dict([(x[1], x[0]) for x in enumerate(alfa)])

# Strips the newline character

total = 0
for line in lines:
    left = line[0:len(line)//2]
    right = line[len(line)//2:]
    #print("{} donne {} et {}".format(line, left, right))
    both = list(set(filter(lambda letter: letter in right, left)))
    #print(both)
    for both_letter in both:
        #print(rdict[both_letter])
        total += rdict[both_letter]
print(total)