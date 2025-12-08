from utils import log, Grid, DIRECTIONS

if __name__ == '__main__':
    file = open('7.txt', 'r')
    lines = file.readlines()
    results = set()
    grid = Grid(lines)
    start = grid.find("S")

    beams = set([start])
    while beams:
        actual = beams.pop()
        next_position = actual.move_with_direction(DIRECTIONS["DOWN"])
        if grid.has(next_position):
            present_char = grid.at(next_position)
            if present_char == "^":
                results.add(next_position)
                left = next_position.move_with_direction(DIRECTIONS["LEFT"])
                if grid.has(left):
                    grid.replace(left, "|")
                    beams.add(left)
                right = next_position.move_with_direction(DIRECTIONS["RIGHT"])
                if grid.has(right):
                    grid.replace(right, "|")
                    beams.add(right)
            else:
                grid.replace(next_position, "|")
                beams.add(next_position)
            #log(grid)
        log(len(results))
    print(len(results))
