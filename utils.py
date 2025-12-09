import logging

DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

EIGHT_DIRECTIONS = {
    "UP": (-1, 0),
    "UP-LEFT": (-1, -1),
    "UP-RIGHT": (-1, 1),
    "DOWN": (1, 0),
    "DOWN-LEFT": (1, -1),
    "DOWN-RIGHT": (1, 1),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

INSTRUCTIONS = {
    "LEFT": '<',
    "RIGHT": '>',
    "UP": '^',
    "DOWN": 'v'
}

ENABLED_LOG = True


def log(text):
    if ENABLED_LOG:
        print(text)


def delete_line():
    print("\033[1A\x1b[2K", end="")


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def distance(self, other):
        return other.row - self.row, other.col - self.col

    def __str__(self):
        return f"Position({self.row}, {self.col})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def move_with_direction(self, direction):
        return Position(self.row + direction[0], self.col + direction[1])

    def get_direction_to(self, other):
        for key, value in DIRECTIONS.items():
            if value == self.distance(other):
                return key
        return None

    def get_instruction_to(self, other):
        for key, value in DIRECTIONS.items():
            if value == self.distance(other):
                return INSTRUCTIONS[key]
        return None


class Grid:
    def __init__(self, lines):
        self.rows = []
        for line in lines:
            self.rows.append([c for c in line])
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def __str__(self):
        return "\n".join("".join(line) for line in self.rows)

    def replace(self, position, char):
        self.rows[position.row][position.col] = str(char)
        return self

    def scan(self):
        positions = []
        for row, line in enumerate(self.rows):
            for col, char in enumerate(line):
                positions.append((char, Position(row, col)))
        return positions

    def at(self, position):
        return self.rows[position.row][position.col]

    def has(self, position):
        return 0 <= position.row < self.height and 0 <= position.col < self.width

    def find(self, char):
        for tile, position in self.scan():
            if tile == char:
                return position

    def find_all(self, char):
        positions = []
        for tile, position in self.scan():
            if tile == char:
                positions.append(position)
        return positions

    def neighbours(self, position, directions=DIRECTIONS):
        neighbours = []
        for direction in directions.values():
            neighbor = position.move_with_direction(direction)
            if self.has(neighbor):
                neighbours.append(neighbor)
        return neighbours
