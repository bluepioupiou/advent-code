from utils import log, Grid, Position, DIRECTIONS, EIGHT_DIRECTIONS

if __name__ == '__main__':
    file = open('7.txt', 'r')
    lines = file.readlines()
    result = 1
    grid = Grid(lines)
    start = grid.find("S")
    first_beam = start.move_with_direction(DIRECTIONS["DOWN"])
    beams = {first_beam: 1}
    for row, line in enumerate(lines[2:], 2):
        new_beams = {}
        for col, char in enumerate(line.strip()):
            cell = Position(row, col)
            #log(f"cell: {cell}")
            if grid.at(cell) == ".":
                total = 0

                left = cell.move_with_direction(DIRECTIONS["LEFT"])
                if grid.has(left) and grid.at(left) == "^":
                    upleft = cell.move_with_direction(EIGHT_DIRECTIONS["UP-LEFT"])
                    if upleft in beams:
                        total += beams[upleft]

                right = cell.move_with_direction(DIRECTIONS["RIGHT"])
                if grid.has(right) and grid.at(right) == "^":
                    upright = cell.move_with_direction(EIGHT_DIRECTIONS["UP-RIGHT"])
                    if upright in beams:
                        total += beams[upright]

                above = cell.move_with_direction(DIRECTIONS["UP"])
                if above in beams:
                    total += beams[above]

                if total:
                    new_beams[cell] = total
        beams = new_beams
        log(f"row {row}: beams: {beams}")
    result = sum(beams.values())
    print(result)
