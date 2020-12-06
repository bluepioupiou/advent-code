file = open('6.txt', 'r')
Lines = file.readlines()

# Strips the newline character
answers = ""
total = 0
for line in Lines:
    if line == "\n":
        #print("{}".format(answers))
        #print("{}".format(set(answers)))
        total += len(set(answers))
        answers = ""
    else:
        answers += line.strip()
print("{}".format(total))
