import re
file = open('5.txt', 'r')
lines = file.readlines()

seeds = [int(x) for x in re.findall('\d+', lines[0].split(":")[1])]
new_seeds = []
for start, range_length in zip(seeds[0::2], seeds[1::2]):
    new_seeds.append((start, start + range_length))
seeds = new_seeds
print(seeds)
total = 0
maps = []
map = None
for line in lines[2::]:
    if "map" in line:
        # Nouvelle map
        map = {"name": line.split(" ")[0], "transitions": []}
    elif line.rstrip() == "":
        # Fin map
        maps.append(map)
    else:
        # Ligne de la map
        destination_start, source_start, range_length = [int(x) for x in re.findall('\d+', line)]
        #print(destination_start, source_start, range_length)
        map["transitions"].append({"min": source_start, "max": source_start + range_length - 1, "change": destination_start - source_start})
maps.append(map)
print(maps)
for map in maps:
    new_seeds = []
    print(f"Running map {map}")
    while seeds:
        seed = seeds.pop()
        print(f" - Analysing seed {seed}")
        for transition in map["transitions"]:
            print(f" -- Analysing transition {transition}")
            new_seed = None
            if transition['min'] <= seed[0] <= seed[1] <= transition['max']:
                print(f" -- Found {seed} entirely in and map to {transition}")
                new_seed = (seed[0] + transition['change'], seed[1] + transition['change'])
                new_seeds.append(new_seed)
                print(f" ---  appending : {new_seed}")
                break
            elif transition['min'] <= seed[0] <= transition['max'] < seed[1]:
                print(f" -- Found {seed} left in for map to {transition}")
                new_seed = (seed[0],  transition['max'])
                remaining_seed = (transition['max'] + 1, seed[1])
                seeds.append(new_seed)
                seeds.append(remaining_seed)
                break
            elif seed[0] < transition['min'] <= seed[1] <= transition['max']:
                print(f" -- Found {seed} right in for map to {transition}")
                new_seed = (transition['min'],  seed[1])
                remaining_seed = (seed[0], transition['min'] - 1)
                seeds.append(new_seed)
                seeds.append(remaining_seed)
                break
            elif seed[0] < transition['min'] <= transition['max'] < seed[1]:
                print(f" -- Found {seed} surrounding map {transition}")
                new_seed = (transition['min'],  transition['max'])
                remaining_left_seed = (seed[0], transition['min'] - 1)
                remaining_right_seed = (transition['max'] + 1, seed[1])
                seeds.append(new_seed)
                seeds.append(remaining_left_seed)
                seeds.append(remaining_right_seed)
                break
        else:
            new_seeds.append(seed)
    seeds = new_seeds
    print(f" --> Seeds after {map['name']} : {seeds}")
print(f"Solution {min(seeds)[0]}")
