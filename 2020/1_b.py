file1 = open('1.txt', 'r') 
Lines = file1.readlines() 
  
# Strips the newline character 
for x in Lines: 
  for y in Lines: 
    for z in Lines: 
      if int(x) + int(y) + int(z) == 2020:
        print("{}".format(int(x) * int(y) * int(z)))
        break
    else:
      continue
    break
  else:
    continue
  break