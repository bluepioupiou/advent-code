file1 = open('1.txt', 'r') 
Lines = file1.readlines() 
  
# Strips the newline character 
for line in Lines: 
  for other_line in Lines: 
    if int(line) + int(other_line) == 2020:
      print("{}".format(int(line) * int(other_line)))
      break
  else:
    continue
  break