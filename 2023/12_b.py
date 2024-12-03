import re
import functools
import itertools
file = open('12.txt', 'r')
lines = file.readlines()


total = 0

print(f"Grid with {len(lines)} rows and {len(lines[0].strip())} cols")

for row, line in enumerate(lines):
    line = line.rstrip()
    records, arrangements = line.split(" ")
    records = "?".join([records, records, records, records, records])
    arrangements = ",".join([arrangements, arrangements, arrangements, arrangements, arrangements])
    arrangements_list = [int(x) for x in arrangements.split(",")]
    regex = ""
    for i, arrangement in enumerate(arrangements_list):
        if i == 0:
            regex += "^\.*"
        regex += "#{" + str(arrangement) + "}"
        if i < len(arrangements_list) - 1:
            regex += "\.+"
    regex += "\.*"

    print(f"records {records} and arrangements {arrangements} for regex {regex}")
    combinations = list(itertools.product('.#', repeat=records.count("?")))
    print(f"- combinations {combinations}")
    for combination in combinations:
        new_line = line
        for character in combination:
            new_line = new_line.replace("?", character, 1)
        if re.search(regex, new_line) and new_line.count("#") == sum(arrangements_list):
            print(f"{new_line} is matching regex")
            total += 1
        # print(f"- possibility {new_line}")

print(f"Solution {total}")
