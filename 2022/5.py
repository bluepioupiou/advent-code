import re
file = open('5.txt', 'r')
lines = file.read().splitlines()

stacks = {}
for line in lines:
    if line == "":
        print(stacks)
    elif line[0:4] == "move":
        params = [int(x) for x in re.findall('[0-9]+', line)]
        print("params {}, take {} from {} to {}".format(params, params[0], stacks[params[1]], stacks[params[2]]))
        for crane in stacks[params[1]][:params[0]]:
            stacks[params[2]].insert(0, crane)
        del stacks[params[1]][:params[0]]
        print(stacks)
    elif line.__contains__("["):
        col = 0
        while len(line) > 0:
            col += 1
            crane = line[:3].strip()
            if crane != "":
                print("found {} row {}".format(crane, col))
                if col not in stacks:
                    stacks[col] = []
                stacks[col].append(crane[1:-1])
            line = line[3:]
            if len(line) > 0:
                line = line[1:]
result = ""
for key in sorted(stacks):
    result += stacks[key][0]

print(result)
