from utils import log, Grid, EIGHT_DIRECTIONS

if __name__ == '__main__':
    file = open('4.txt', 'r')
    lines = file.readlines()
    result = 0

    grid = Grid(lines)
    while True:
        rolls_to_remove = []
        for char, position in grid.scan():
            if char == "@":
                number_of_rolls = 0
                for neighbor in grid.neighbours(position, EIGHT_DIRECTIONS):
                    #log(f"neighbor {neighbor} with value {grid.at(neighbor)}")
                    if grid.at(neighbor) == "@":
                        number_of_rolls += 1
                #log(f"position {position} has {number_of_rolls} rolls neigbours")
                if number_of_rolls < 4:
                    rolls_to_remove.append(position)
        if not rolls_to_remove:
            break
        log(f"Remove {len(rolls_to_remove)} rolls")
        for roll in rolls_to_remove:
            grid.replace(roll, "x")
        log(f"Grid résultat : \n {grid}")
    print(len(list(filter(lambda x: x[0] == 'x', grid.scan()))))
