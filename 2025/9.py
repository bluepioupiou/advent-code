from utils import log, Grid, Position, DIRECTIONS
import math
import itertools

if __name__ == '__main__':
    file = open('9.txt', 'r')
    lines = file.readlines()
    #grid = Grid(lines)
    #corners = grid.find_all("#")
    corners = [Position(int(x[0]), int(x[1])) for x in [line.strip().split(",") for line in lines]]
    log(f"corners: {corners}")
    best_area = 0
    for corner1, corner2 in itertools.combinations(corners, 2):
        area = (abs(corner1.row - corner2.row) + 1) * (abs(corner1.col - corner2.col) + 1)
        log(f"area for {corner1} and {corner2} is {area}")
        best_area = max(best_area, area)
    print(best_area)
