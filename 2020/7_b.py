file = open('7.txt', 'r')
Lines = file.readlines()


def deep_count_for(bag, bags):
    total = 1
    for new_bag, bag_count in bags[bag].items():
        total += bag_count * deep_count_for(new_bag, bags)
    print("{} represents {} bags".format(bag, total))
    return total

# Strips the newline character
collections = {}
for line in Lines:
    key, values = line.strip()[:-1].split("s contain ")
    values = values.split(", ")
    contains = {}
    for value in values:
        parts = value.strip().split(" ")
        if parts[0] != "no":
            count = int(parts[0])
            if count > 1:
                parts[-1] = parts[-1][:-1]
            name = " ".join(parts[1:])
            #print("{} {} in {}".format(count, name, key))
            contains[name] = count
    collections[key] = contains
print("{}".format(collections))
total = deep_count_for("shiny gold bag", collections)


print("{}".format(total-1))

