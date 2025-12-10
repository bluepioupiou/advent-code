from utils import log, Grid, Position, DIRECTIONS
import math
import itertools
from shapely.geometry import Polygon, box

if __name__ == '__main__':
    file = open('9.txt', 'r')
    lines = file.readlines()
    corners = [tuple(map(int, line.strip().split(","))) for line in lines]
    floor = Polygon(corners)
    best_area = 0

    for corner1, corner2 in itertools.combinations(corners, 2):
        log(f"testing {corner1} and {corner2}")
        x1, y1 = corner1
        x2, y2 = corner2
        # On anticipe les deux angles restants pour tester si ils sont dedans
        rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        #log(box)
        if floor.covers(rectangle):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            #log(f"  --> area for {corner1} and {corner2} is {area}")
            best_area = max(best_area, area)

        #log("")
    print(best_area)
