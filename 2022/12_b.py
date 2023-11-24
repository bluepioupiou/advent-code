import math
file = open('12.txt', 'r')
lines = file.read().splitlines()
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
map = []
starts_positions = []
map_start = None
map_end = None
heights = "abcdefghijklmnopqrstuvwxyz"
for row, line in enumerate(lines):
    col = line.find("S")
    if col > -1:
        map_start = (row, col)
    col = line.find("E")
    if col > -1:
        map_end = (row, col)
    line = line.replace("S", "a")
    line = line.replace("E", "z")
    for col, char in enumerate(line):
        if char == "a":
            starts_positions.append((row, col))
    map.append(line)

rows_count = len(map)
cols_count = len(map[0])
print("Map start: {}".format(map_start))
print("Map end: {}".format(map_end))
#print("Starting positions {}".format(starts_positions))
best_path = 999
for map_start in starts_positions:
    visited = [map_start]
    heads = [map_start]
    cycle = 0
    finished = False
    while not finished:
        cycle += 1
        new_heads = []
        if len(heads) == 0:
            cycle = -1
            finished = True
        for current_tile in heads:
            current_height = map[current_tile[0]][current_tile[1]]
            # On vérifie les tuiles de toutes les directions
            for direction in directions:
                new_tile = (current_tile[0] + direction[0], current_tile[1] + direction[1])
                # Si ça sort de la carte --> ignore
                if new_tile[0] < 0 or new_tile[0] >= rows_count or new_tile[1] < 0 or new_tile[1] >= cols_count:
                    continue
                new_height = map[new_tile[0]][new_tile[1]]
                # Si trop haut pour y grimper --> ignore
                if heights.index(new_height) - heights.index(current_height) > 1:
                    continue
                # Si déjà visitée --> ignore
                if new_tile in visited:
                    continue
                if new_tile == map_end:
                    best_path = min(cycle, best_path)
                    finished = True

                new_heads.append(new_tile)
                visited.append(new_tile)
        heads = new_heads
        #print("Cycle {} etat des tetes de parcours {} (parcourus {})".format(cycle, heads, len(visited)))


    print("Trouvé au cycle {}".format(cycle))
print("meilleur chemin en {}".format(best_path))
