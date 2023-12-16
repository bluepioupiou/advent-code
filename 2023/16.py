
DIRECTION_RIGHT = (0, 1)
DIRECTION_LEFT = (0, -1)
DIRECTION_UP = (-1, 0)
DIRECTION_DOWN = (1, 0)


class Ray:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __repr__(self):
        return f"{self.position}:{self.direction}"

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction

    def get_next_position(self):
        return self.position[0] + self.direction[0], self.position[1] + self.direction[1]


def change_in_pattern(pattern, row, column, char):
    pattern[row] = pattern[row][:column] + char + pattern[row][column + 1:]

mirrors = {
    "/": {
        DIRECTION_RIGHT: [DIRECTION_UP],
        DIRECTION_DOWN: [DIRECTION_LEFT],
        DIRECTION_UP: [DIRECTION_RIGHT],
        DIRECTION_LEFT: [DIRECTION_DOWN]
    },
    "\\": {
        DIRECTION_RIGHT: [DIRECTION_DOWN],
        DIRECTION_DOWN: [DIRECTION_RIGHT],
        DIRECTION_UP: [DIRECTION_LEFT],
        DIRECTION_LEFT: [DIRECTION_UP]
    },
    "|": {
        DIRECTION_RIGHT: [DIRECTION_UP, DIRECTION_DOWN],
        DIRECTION_DOWN: [DIRECTION_DOWN],
        DIRECTION_UP: [DIRECTION_UP],
        DIRECTION_LEFT: [DIRECTION_UP, DIRECTION_DOWN]
    },
    "-": {
        DIRECTION_RIGHT: [DIRECTION_RIGHT],
        DIRECTION_DOWN: [DIRECTION_LEFT, DIRECTION_RIGHT],
        DIRECTION_UP: [DIRECTION_LEFT, DIRECTION_RIGHT],
        DIRECTION_LEFT: [DIRECTION_LEFT]
    },
    ".": {
        DIRECTION_RIGHT: [DIRECTION_RIGHT],
        DIRECTION_DOWN: [DIRECTION_DOWN],
        DIRECTION_UP: [DIRECTION_UP],
        DIRECTION_LEFT: [DIRECTION_LEFT]
    }
}

if __name__ == '__main__':
    file = open('16.txt', 'r')
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    energy_map = ["." * len(lines[0].rstrip()) for line in lines]
    ray = Ray((0, -1), (0, 1))
    rays = [ray]
    passed = []
    while len(rays):
        ray = rays.pop()
        next_position = ray.get_next_position()
        #print(f"Trying ray to {next_position}")
        if 0 <= next_position[0] < len(lines) and 0 <= next_position[1] < len(lines[0]):
            change_in_pattern(energy_map, next_position[0], next_position[1], "#")
            next_mirror = mirrors[lines[next_position[0]][next_position[1]]]
            next_ray_directions = next_mirror[ray.direction]
            for direction in next_ray_directions:
                new_ray = Ray(next_position, direction)
                if new_ray not in passed:
                    passed.append(new_ray)
                    rays.append(new_ray)
            #print(f"rays : {rays}")
    total = 0
    for line in energy_map:
        print(line)
        total += line.count("#")
    print(f"Total {total}")