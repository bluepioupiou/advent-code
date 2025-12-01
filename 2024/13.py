from utils import log, Grid, Position, DIRECTIONS

file = open('12.txt', 'r')
lines = file.readlines()

total = 0
if __name__ == '__main__':
    grid = Grid(lines)
    tiles = grid.scan()
    already_scanned = []
    while tiles:
        plant, position = tiles.pop(0)
        if position not in already_scanned:
            log(f"Analysing {plant} at {position}")
            perimeter = 0
            area = 0
            to_search = [position]
            region = []
            while to_search:
                tile = to_search.pop()
                new_perimeter = 0
                # Calculate impact of tile
                neighbours = grid.neighbours(tile)
                area += 1
                new_perimeter += 4 - len(neighbours)
                region.append(tile)
                already_scanned.append(tile)
                #log(f" - region {region}")
                for neighbor in neighbours:
                    #log(f"{neighbor} not in {region} ? {neighbor not in region}")
                    if neighbor not in to_search and neighbor not in region:
                        neighbor_plant = grid.at(neighbor)
                        if neighbor_plant == plant:
                            to_search.append(neighbor)
                        else:
                            new_perimeter += 1
                #log(f" - new tile at {tile} for region {plant} with perimeter {new_perimeter}")
                perimeter += new_perimeter
            log(f"Found region of {plant} with area {area} and perimeter {perimeter}")
            total += area * perimeter
    print(total)