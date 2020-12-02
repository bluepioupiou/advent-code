file1 = open('2.txt', 'r') 
Lines = file1.readlines() 
  
count_valid_passwords = 0
# Strips the newline character 
for line in Lines: 
  rules, password = line.split(":")
  numbers, letter = rules.split(" ")
  min, max = numbers.split("-")
  #print("{} {} {} {}".format(min, max, letter, password))
  if int(min) <= password.count(letter) <= int(max):
    count_valid_passwords += 1

print("{}".format(count_valid_passwords))
