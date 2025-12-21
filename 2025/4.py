from utils import log, Grid, EIGHT_DIRECTIONS

if __name__ == '__main__':
    file = open('4.txt', 'r')
    lines = file.readlines()
    result = 0

    grid = Grid(lines)
    for position in grid.scan():
        #log(f"position {position}")
        if grid.at(position[1]) == "@":
            number_of_rolls = 0
            for neighbor in grid.neighbours(position[1], EIGHT_DIRECTIONS):
                log(f"neighbor {neighbor} with value {grid.at(neighbor)}")
                if grid.at(neighbor) == "@":
                    number_of_rolls += 1
            log(f"position {position} has {number_of_rolls} rolls neigbours")
            if number_of_rolls < 4:
                result += 1

    print(result)
