directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}


def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]


def find_enclosed_areas(pattern):
    sweeped = []

    for row, line in enumerate(pattern):
        for col, c in enumerate(line):
            if c == "." and (row, col) not in sweeped:
                #print(f"New tile not swept yet {(row, col)}")
                area_sweeped = []
                area_characters = []
                to_swep = [(row, col)]
                while len(to_swep):
                    position = to_swep.pop()
                    area_sweeped.append(position)
                    area_characters.append(pattern[position[0]][position[1]])

                    for direction_name, direction in directions.items():
                        neighbour_position = (
                            min(len(pattern) - 1, max(0, position[0] + direction[0])),
                            min(len(pattern[0]) - 1, max(0, position[1] + direction[1]))
                        )
                        # print(f"-- checking {neighbour_position}")
                        if neighbour_position not in area_sweeped \
                                and neighbour_position not in to_swep \
                                and pattern[neighbour_position[0]][neighbour_position[1]] in ["."]:
                            to_swep.append(neighbour_position)
                    # print(f"- area sweeped {area_sweeped}")
                    # print(f"- to_swep {to_swep}")
                #print(f"Total area sweeped {area_sweeped}")
                #print(f"Total area characters {area_characters}")
                for position in area_sweeped:
                    if position[0] in [0, len(pattern) - 1] or position[1] in [0, len(pattern[0]) - 1]:
                        #print(f"Nope, this one is not closed {len(area_sweeped)}")
                        break
                else:
                    #print(f"Hourra, we found an enclosed group {len(area_sweeped)}")
                    for position in area_sweeped:
                        if pattern[position[0]][position[1]] == ".":
                            change_in_pattern(pattern, position[0], position[1], "#")
                sweeped += area_sweeped


if __name__ == '__main__':
    file = open('18.txt', 'r')
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    position = (0, 0)
    min_row = max_row = min_col = max_col = 0
    digs = []
    for line in lines:
        direction, distance, color = line.split(" ")
        digs.append((direction, distance))
        for meter in range(int(distance)):
            position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
            min_row = min(min_row, position[0])
            max_row = max(max_row, position[0])
            min_col = min(min_col, position[1])
            max_col = max(max_col, position[1])
        print(f"Position {position} after {direction} and {distance}")
    print(f"row from {min_row} to {max_row} and col from {min_col} to {max_col}")
    plan = ["." * (max_col - min_col + 1) for x in range(max_row - min_row + 1)]

    #for line in plan:
    #    print(line)

    position = (- min_row, - min_col)
    change_in_pattern(plan, position[0], position[1], "#")
    for direction, distance in digs:
        for meter in range(int(distance)):
            #print(f"Advancing direction {direction} for meter {meter} for position {position}")
            position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
            change_in_pattern(plan, position[0], position[1], "#")
    print("")
    for line in plan:
        print(line)
    print("")
    find_enclosed_areas(plan)
    result = 0
    for line in plan:
        print(line)
        result += line.count("#")
    print(f"Result {result}")
