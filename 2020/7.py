file = open('7.txt', 'r')
Lines = file.readlines()

# Strips the newline character
collections = {}
for line in Lines:
    key, values = line.strip()[:-1].split("s contain ")
    values = values.split(", ")
    names = []
    for value in values:
        parts = value.strip().split(" ")
        if parts[0] != "no":
            count = int(parts[0])
            if count > 1:
                parts[-1] = parts[-1][:-1]
            name = " ".join(parts[1:])
            #print("{} {} in {}".format(count, name, key))
            if name not in collections:
                collections[name] = [key]
            else:
                collections[name].append(key)

#print("{}".format(collections))

to_find = ["shiny gold bag"]
definitely_found_in = set()
while len(to_find):
    next_to_find = []
    for item in to_find:
        if item in collections:
            found_in = set(collections[item])
            definitely_found_in = definitely_found_in.union(found_in)
            next_to_find += found_in
    to_find = next_to_find

print("{}".format(definitely_found_in))
print("{}".format(len(definitely_found_in)))
