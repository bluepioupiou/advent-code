file = open('6.txt', 'r')
Lines = file.readlines()

# Strips the newline character
answers = {}
count_answers = 0
total = 0

for line in Lines:
    if line == "\n":
        #print("{} for {}".format(answers, count_answers))
        for count in answers.values():
            if count == count_answers:
                total += 1
        answers = {}
        count_answers = 0
    else:
        count_answers += 1
        for answer in line.strip():
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1
print("{}".format(total))
