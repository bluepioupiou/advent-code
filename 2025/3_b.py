from utils import log
import itertools

if __name__ == '__main__':
    file = open('3.txt', 'r')
    lines = file.readlines()
    result = 0

    for line in lines:
        line = line.strip()
        batteries = []
        start_position = 0
        log(f"{line} ({len(line)})")
        for char in range(0, 12):
            best_battery = 0
            best_position = 0
            max = len(line) - 12 + char
            min = start_position
            log(f"Analysing between {min} and {max} -> {line[min:max + 1]}")
            for position in range(max, min - 1, -1):
                battery = int(line[position])
                log(f" - {battery} better thant {best_battery} ? ")
                if battery >= best_battery:
                    #log(f" - yes !")
                    best_battery = battery
                    best_position = position

            batteries.append(str(best_battery))
            start_position = best_position + 1
            log(f" - best is {best_battery} at position {best_position}")
        log(batteries)
        max_joltage = int("".join(batteries))
        log(f"Max joltage is {max_joltage}")
        result += max_joltage

    print(result)
