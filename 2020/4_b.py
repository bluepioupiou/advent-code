import re

file = open('4.txt', 'r')
Lines = file.readlines()
  
# Strips the newline character
mandatories = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
document = ""
valid = 0
for line in Lines:
    if line == "\n":
        fields = document.split()


        for field in fields:
            key, value = field.split(":")
            if key == "byr":
                if int(value) < 1920 or int(value) > 2002:
                    break
            elif key == "iyr":
                if int(value) < 2010 or int(value) > 2020:
                    break
            elif key == "eyr":
                if int(value) < 2020 or int(value) > 2030:
                    break
            elif key == "hgt":
                if "cm" in value:
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        break
                elif "in" in value:
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        break
                else:
                    break
            elif key == "hcl":
                if not re.search("^#([a-fA-F0-9]{6})$", value):
                    break
            elif key == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    break
            elif key == "pid":
                if not re.search("^([0-9]{9})$", value):
                    break
        else:
            for mandatory in mandatories:
                if mandatory + ":" not in document:
                    break
            else:
                valid += 1
        document = ""
    else:
        document += " " + line.strip()
print("{}".format(valid))