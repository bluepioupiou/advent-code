import re
file = open('5.txt', 'r')
lines = file.readlines()

seeds = [int(x) for x in re.findall('\d+', lines[0].split(":")[1])]
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
        map["transitions"].append({"min": source_start, "max": source_start + range_length, "change": destination_start - source_start})
maps.append(map)
print(maps)
for map in maps:
    for position, seed in enumerate(seeds):
        for transition in map["transitions"]:
            if transition['min'] <= seed <= transition['max']:
                print(f"Found {seed} and position {position} and map to {seed + transition['change']}")
                seeds[position] = seed + transition['change']
    print(f"Seeds after {map['name']} : {seeds}")
print(f"Solution {min(seeds)}")
