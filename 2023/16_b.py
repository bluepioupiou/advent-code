
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
    possible_starts = []
    for row in range(len(lines)):
        possible_starts.append(Ray((row, -1), DIRECTION_RIGHT))
        possible_starts.append(Ray((row, len(lines[0])), DIRECTION_LEFT))
    for col in range(len(lines[0])):
        possible_starts.append(Ray((-1, col), DIRECTION_DOWN))
        possible_starts.append(Ray((len(lines), col), DIRECTION_UP))

    best = 0
    for starting_ray in possible_starts:
        energy_map = ["." * len(lines[0].rstrip()) for line in lines]
        rays = [starting_ray]
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
            # print(line)
            total += line.count("#")
        best = max(total, best)
        print(f"total for starting ray {starting_ray} :  {total}")
    print(f"best {best}")
