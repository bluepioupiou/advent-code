from utils import log, Grid, Position, DIRECTIONS

file = open('10.txt', 'r')
lines = file.readlines()

total = 0
if __name__ == '__main__':
    grid = Grid(lines)
    for char, position in grid.scan():
        if char == "0":
            trailheads = 0
            paths = [position]
            while paths:
                path_position = paths.pop(0)
                #log(f"Analysing position {path_position} with value {int(grid.at(path_position))}")
                for neighbour in grid.neighbours(path_position):
                    if grid.at(neighbour) != ".":
                        difference = int(grid.at(neighbour)) - int(grid.at(path_position))
                        #log(f" - neighbor {neighbour} with value {grid.at(neighbour)} and difference {difference}")
                        if difference == 1:
                            if grid.at(neighbour) == "9":
                                #log(f" |- FINAL position {neighbour} that is a 9")
                                trailheads += 1
                                continue
                            #log(f" |- Found next position {neighbour}")
                            paths.append(neighbour)
            log(f"{trailheads} for starting position {position}")
            total += trailheads

    print(total)