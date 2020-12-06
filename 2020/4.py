file = open('4.txt', 'r')
Lines = file.readlines()
  
# Strips the newline character
mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
document = ""
valid = 0
for line in Lines:
    if line == "\n":
        fields = document.split()
        for field in fields:
            key, value = field.split(":")
        else:
            valid += 1
        document = ""
    else:
        document += " " + line.strip()
print("{}".format(valid))