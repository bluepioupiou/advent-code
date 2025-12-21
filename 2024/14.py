from utils import log, Grid, Position, DIRECTIONS
import re

file = open('14.txt', 'r')
lines = file.readlines()

wide = 11
tall = 7

init = ["".join(["."] * wide) for x in range(tall)]

robots = []
total = 0


class Robot:

    def __init__(self, x, y, vx, vy):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)

    def __str__(self):
        return f"Robot(Position({self.x}, {self.y}) et vitesse ({self.vx}, {self.vy})"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    grid = Grid(init)
    log(grid)
    for line in lines:
        search = re.search("p=(\d*),(\d*) v=(-?\d*),(-?\d)*", line)
        x, y, vx, vy = search.groups()
        robots.append(Robot(x, y, vx, vy))
    log(robots)
    for second in range(100):
        grid = Grid(init)
        for index, robot in enumerate(robots):
            new_robot = Robot((robot.x + robot.vx) % wide, (robot.y + robot.vy) % tall, robot.vx, robot.vy)
            #log(f" - new robot {new_robot}")
            robots[index] = new_robot
            position = Position(new_robot.y, new_robot.x)
            already = grid.at(position)
            if already == ".":
                already = 1
            else:
                already = str(int(already) + 1)
                if int(already) > 9:
                    print("XXXXXXXXXXXXXXXXXXXXXX")
            grid.replace(position, already)
        log(f"Second {second} => \n{grid}")
    quadrant_left_up = 0
    quadrant_right_up = 0
    quadrant_left_down = 0
    quadrant_right_down = 0
    for tile, position in grid.scan():
        if not tile == ".":
            if position.col < wide // 2:
                if position.row < tall // 2:
                    log(f" - found {tile} in left_up at {position}")
                    quadrant_left_up += int(tile)
                elif position.row > tall // 2:
                    log(f" - found {tile} in left_down at {position}")
                    quadrant_left_down += int(tile)
            elif position.col > wide // 2:
                if position.row < tall // 2:
                    log(f" - found {tile} in right_up at {position}")
                    quadrant_right_up += int(tile)
                elif position.row > tall // 2:
                    log(f" - found {tile} in right_down at {position}")
                    quadrant_right_down += int(tile)

    log(f"left_up: {quadrant_left_up}, right_up: {quadrant_right_up}, left_down: {quadrant_left_down}, right_down: {quadrant_right_down}")
    print(quadrant_left_up * quadrant_right_up * quadrant_left_down * quadrant_right_down)