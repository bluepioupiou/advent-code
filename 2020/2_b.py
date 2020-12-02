file1 = open('2.txt', 'r') 
Lines = file1.readlines() 
  
count_valid_passwords = 0
# Strips the newline character 
for line in Lines: 
  rules, password = line.split(":")
  numbers, letter = rules.split(" ")
  min, max = numbers.split("-")
  #print("{} {} {} {}".format(min, max, letter, password))
  score = 0
  if password[int(min)] == letter:
    score+= 1
  if password[int(max)] == letter:
    score += 1
  if score == 1:
    #print("{} is valid for letter {} because {} or {}".format(line, letter, password[int(min)], password[int(max)]))
    count_valid_passwords += 1
  #else:
    #print("{} is not for letter {} because {} or {}".format(line, letter, password[int(min)], password[int(max)]))


print("{}".format(count_valid_passwords))
