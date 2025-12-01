from utils import log, Grid, Position, DIRECTIONS
import re

file = open('13.txt', 'r')
lines = file.readlines()

wide = 11
tall = 7

init = ["".join(["."] * wide) for x in range(tall)]

robots = []
total = 0
if __name__ == '__main__':
    grid = Grid(init)
    print(grid)
    for line in lines:
        search = re.search("p=(\d*),(\d*) v=(-?\d*),(-?\d)*", line)
        x, y, vx, vy = search.groups()
        robots.append((x, y, vx, vy))
        for second in range(100):
            grid = Grid(init)
            for index, robot in enumerate(robots):
                new_robot = ((robot.x + robot.vx) % wide, (robot.y + robot.vy) % tall, robot.vx, robot.vy)
                robots[index] = new_robot

