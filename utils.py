DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"Position {self.row}, {self.col}"

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def move_with_direction(self, direction):
        return Position(self.row + direction[0], self.col + direction[1])


class Grid:
    def __init__(self, lines):
        self.rows = []
        for line in lines:
            self.rows.append([c for c in line.replace("\n", "")])
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def __str__(self):
        return "\n".join("".join(line) for line in self.rows)

    def replace(self, position, char):
        self.rows[position.row][position.col] = char
        return self

    def get_positions(self):
        positions = []
        for row, line in enumerate(self.rows):
            for col, char in enumerate(line):
                positions.append((char, row, col))
        return positions

    def at(self, position):
        return self.rows[position.row][position.col]

    def has_position(self, position):
        return 0 <= position.row < self.height and 0 <= position.col < self.width
