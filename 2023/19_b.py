import re
from copy import deepcopy

class Part:

    def __init__(self, numbers):
        self.x = numbers[0]
        self.m = numbers[1]
        self.a = numbers[2]
        self.s = numbers[3]

    def get(self, letter):
        if letter == "x":
            return self.x
        if letter == "m":
            return self.m
        if letter == "a":
            return self.a
        if letter == "s":
            return self.s

    def total(self):
        return int(self.x) + int(self.m) + int(self.a) + int(self.s)

    def __str__(self):
        return f"x: {self.x}, m: {self.m}, a: {self.a}, s: {self.s}"

    def __repr__(self):
        return f"({self.x}, {self.m}, {self.a}, {self.s})"


class Workflow:

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules.split(",")

    def __str__(self):
        return f"name: {self.name}, rules: {self.rules}"

    def __repr__(self):
        return f"({self.name}, {self.rules}"

    def get_output(self, part: Part):
        for rule in self.rules[:-1]:
            condition, output = rule.split(":")
            condition = part.get(condition[0]) + condition[1:]
            print(f"condition : {condition}")
            if eval(condition):
                return output
        return self.rules[-1]

    def get_part_ranges(self, part_range):
        part_ranges = []
        for rule in self.rules[:-1]:
            condition, output = rule.split(":")
            variable = condition[0]
            operand = condition[1]
            number = int(condition[2:])
            if operand == "<":
                if part_range[f"{variable}_min"] < number:
                    new_part_range = deepcopy(part_range)
                    new_part_range[f"{variable}_max"] = min(new_part_range[f"{variable}_max"], number - 1)
                    part_range[f"{variable}_min"] = number
                    new_part_range["workflow"] = output
                    part_ranges.append(new_part_range)
            elif operand == ">":
                if part_range[f"{variable}_max"] > number:
                    new_part_range = deepcopy(part_range)
                    new_part_range[f"{variable}_min"] = max(new_part_range[f"{variable}_min"], number + 1)
                    part_range[f"{variable}_max"] = number
                    new_part_range["workflow"] = output
                    part_ranges.append(new_part_range)

        part_range["workflow"] = self.rules[-1]
        part_ranges.append(part_range)
        print(f" - {part_ranges}")
        return part_ranges


if __name__ == '__main__':
    file = open('19.txt', 'r')
    result = 0
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    workflows = {}
    parts = []
    for line in lines:
        if line.startswith("{"):
            numbers = re.findall("\d+", line)
            parts.append(Part(numbers))
        elif line.endswith("}"):
            name, rules = line.split("{")
            workflows[name] = (Workflow(name, rules[:-1]))

    part_ranges = [{"workflow": "in", "x_min": 1, "x_max": 4000, "m_min": 1, "m_max": 4000, "a_min": 1, "a_max": 4000, "s_min": 1, "s_max": 4000}]
    while part_ranges:
        actual_part_range = part_ranges.pop(0)
        print(f"Actual range {actual_part_range}")
        new_part_ranges = workflows[actual_part_range["workflow"]].get_part_ranges(actual_part_range)
        for part_range in new_part_ranges:
            if part_range["workflow"] == "A":
                print(f"--> accepted {part_range}")
                result += (part_range["x_max"] - part_range["x_min"] + 1) \
                    * (part_range["m_max"] - part_range["m_min"] + 1) \
                    * (part_range["a_max"] - part_range["a_min"] + 1) \
                    * (part_range["s_max"] - part_range["s_min"] + 1)
            elif part_range["workflow"] == "R":
                print(f"--> refused {part_range}")
            else:
                part_ranges.append(part_range)

    # print(workflows)
    print(f"Result { result}")
