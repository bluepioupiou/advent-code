from utils import log, delete_line, Grid, Position, DIRECTIONS, INSTRUCTIONS
import re
from functools import cache

file = open('19.txt', 'r')
lines = file.readlines()

total = 0


if __name__ == '__main__':
    towels = set([x.replace("\n", "") for x in lines[0].split(", ")])


    @cache
    def is_possible(design: str):
        return (
                design == ''
                or any(
            design.startswith(towel)
            and is_possible(design[len(towel):])
            for towel in towels
        )
    )


    for line in lines[2:]:
        line = line.replace("\n", "")
        log(f"Trying {line}")
        if is_possible(line):
            total += 1
    print(total)
