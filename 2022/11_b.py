import math
file = open('11.txt', 'r')
lines = file.read().splitlines()

monkeys = []
monkey = None
for line in lines:
    line = line.strip()
    if line.startswith("Monkey"):
        monkey = {"inspected": 0}
    elif line.startswith("Starting"):
        items = [int(x) for x in line.split(":")[1].strip().split(", ")]
        monkey["items"] = items
    elif line.startswith("Operation"):
        monkey["operation"] = line.split("=")[1].strip()
    elif line.startswith("Test"):
        monkey["divisible"] = int(line.split("by")[1].strip())
    elif line.startswith("If true"):
        monkey["true"] = int(line.split("monkey")[1].strip())
    elif line.startswith("If false"):
        monkey["false"] = int(line.split("monkey")[1].strip())
    elif line == "":
        monkeys.append(monkey)
#print(monkeys)
common = 1
for monkey in monkeys:
    common *= monkey["divisible"]
print(common)
actual_round = 0
while actual_round < 20:
    actual_round += 1
    for count, monkey in enumerate(monkeys):
        #print("Monkey {}".format(count))
        for item in monkey["items"]:
            #print("  Monkey inspects an item with a worry level of {}".format(monkey["items"]))
            result = eval(monkey["operation"].replace("old", str(item)))
            #print("    Worry level calculated by {} to {}".format(monkey["operation"], result))
            #result = math.floor(result / 3)
            #print("    Monkey gets bored with item. Worry level is divided by 3 to {}".format(result))
            if result % monkey["divisible"] == 0:
                monkeys[monkey["true"]]["items"].append(result)
                #print("    Current worry level is divisible by {}".format(monkey["divisible"]))
                #print("    Item with worry level {} is thrown to monkey {}".format(result, monkey["true"]))
            else:
                monkeys[monkey["false"]]["items"].append(result)
                #print("    Current worry level is not divisible by {}".format(monkey["divisible"]))
                #print("    Item with worry level {} is thrown to monkey {}".format(result, monkey["false"]))
            monkey["inspected"] += 1

        monkey["items"] = []
    for monkey in monkeys:
        for i in range(0, len(monkey["items"])):
            if monkey["items"][i] % common == 0:
                monkey["items"][i] = monkey["items"][i] / common

    if actual_round % 20 == 0:
        print("After round {}".format(actual_round))
        for count, monkey in enumerate(monkeys):
            print("Monkey {}: {} --> {}".format(count, monkey["items"], monkey["inspected"]))

