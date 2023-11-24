file = open('3.txt', 'r')
lines = file.read().splitlines()

alfa = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define reverse lookup dict
rdict = dict([(x[1], x[0]) for x in enumerate(alfa)])

# Strips the newline character

total = 0
for one, two, three in zip(lines[0::3], lines[1::3], lines[2::3]):
    common = list(set(filter(lambda letter: letter in two and letter in three, one)))
    #print(both)
    for common_letter in common:
        #print(rdict[both_letter])
        total += rdict[common_letter]
print(total)