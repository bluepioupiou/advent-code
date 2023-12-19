import re


class Part:

    def __init__(self, numbers):
        self.x = numbers[0]
        self.m = numbers[1]
        self.a = numbers[2]
        self.s = numbers[3]

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
            condition.replace("x", part.x)
            condition.replace("m", part.m)
            condition.replace("a", part.a)
            condition.replace("s", part.s)
            print(f"condition > {condition}")
            if eval(condition):
                return output
        return rules[-1]

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

    for part in parts:
        print(f"Evaluating part ")
        actual_workflow = workflows["in"]
        output = None
        while output not in ["A", "R"]:

            output = actual_workflow.get_output(part)
            actual_workflow = workflows[output]

    print(parts)
    print(workflows)
    print(f"Result { result}")
