from utils import Grid, Position, DIRECTIONS

file = open('6.txt', 'r')
lines = file.readlines()

total = 0
directions = [DIRECTIONS["UP"], DIRECTIONS["RIGHT"], DIRECTIONS["DOWN"], DIRECTIONS["LEFT"]]
direction = 0
initial_lines = []
initial_position = None

if __name__ == '__main__':
    grid = Grid(lines)
    #print(grid)

    for char, row, col in grid.get_positions():
        if char == "^":
            initial_position = Position(row, col)
            grid.replace(initial_position, ".")
    #print(grid)
    # On fait tout le chemin 'normal' jusqu'au bout
    position = Position(initial_position.row, initial_position.col)
    initial_path = []
    while True:
        new_position = position.move_with_direction(directions[direction])
        if not grid.has_position(new_position):
            break
        if grid.at(new_position) == "#":
            direction = (direction + 1) % 4
        else:
            position = new_position
            initial_path.append((position, direction))

    working_obstacles = set()
    for index, obstacle_position in enumerate([x[0] for x in initial_path if x[0] != initial_position]):
        position = Position(initial_position.row, initial_position.col)
        direction = 0
        grid.replace(obstacle_position, "#")
        print(f"Putting obstacle at {obstacle_position}")
        paths = []

        while True:
            new_position = position.move_with_direction(directions[direction])
            if not grid.has_position(new_position):
                break
            if grid.at(new_position) == "#":
                direction = (direction + 1) % 4
            else:
                position = new_position
                if (position, direction) in paths:
                    working_obstacles.add(obstacle_position)
                    break
                paths.append((position, direction))
        grid.replace(obstacle_position, ".")

    print(f"\n{len(working_obstacles)}")
