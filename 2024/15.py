from utils import log, Grid, Position, DIRECTIONS
import re

file = open('15.txt', 'r')
lines = file.readlines()

total = 0

INSTRUCTIONS = {
    '<': "LEFT",
    '>': "RIGHT",
    '^': "UP",
    'v': "DOWN"
}
if __name__ == '__main__':
    grid_lines = []
    instructions_line = ""
    for line in lines:
        if '#' in line:
            grid_lines.append(line)
        elif '<' in line:
            instructions_line += line.replace("\n", "")
    grid = Grid(grid_lines)
    log(grid)
    log(instructions_line)

    robot_position = grid.find("@")
    for instruction in instructions_line:
        direction = DIRECTIONS[INSTRUCTIONS[instruction]]
        log(f"Move {instruction} {direction}")
        next_position = robot_position.move_with_direction(direction)
        if grid.at(next_position) == ".":
            grid.replace(robot_position, ".")
            grid.replace(next_position, "@")
            robot_position = next_position
        else:
            boxes = []
            while grid.at(next_position) == "O":
                boxes.append(next_position)
                next_position = next_position.move_with_direction(direction)
            if grid.at(next_position) == ".":
                grid.replace(next_position, "O")
                grid.replace(boxes[0], "@")
                grid.replace(robot_position, ".")
                robot_position = boxes[0]
        log(grid)
        total = 0
    for char, position in grid.scan():
        if char == "O":
            total += 100 * position.row + position.col
    print(total)