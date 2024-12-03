import re
import functools
file = open('8.txt', 'r')
lines = file.readlines()

directions = lines[0].rstrip()
nodes = {}
actual_nodes = []
for node in lines[2:]:
    start, possibilities = node.split(" = ")
    possibilities = possibilities[1:-2].split(", ")
    nodes[start] = possibilities
    if "A" in start:
        actual_nodes.append(start)

print(f"nodes {nodes}")

steps = 0
print(f"Your are on {actual_nodes}")
while len(list(filter(lambda x: "Z" not in x, actual_nodes))) > 0:
    next_direction = directions[steps % len(directions)]
    next_nodes = []
    for actual_node in actual_nodes:
        follow_nodes = nodes[actual_node]
        if next_direction == "L":
            next_node = follow_nodes[0]
        else:
            next_node = follow_nodes[1]
        #print(f" - Step {steps}, going from {actual_node} with direction {next_direction} to {next_node}")

        next_nodes.append(next_node)
    #print(f" - Step {steps}: You choose all of the {next_direction} paths, leading you to {next_nodes}.")
    actual_nodes = next_nodes
    steps += 1
    if not steps % 10000:
        print(steps)

print(f"Solution {steps}")
