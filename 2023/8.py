import re
import functools
file = open('8.txt', 'r')
lines = file.readlines()

directions = lines[0].rstrip()
nodes = {}

for node in lines[2:]:
    start, possibilities = node.split(" = ")
    possibilities = possibilities[1:-2].split(", ")
    nodes[start] = possibilities

print(f"nodes {nodes}")

actual_node = "AAA"
steps = 0

while actual_node != "ZZZ":
    next_direction = directions[steps % len(directions)]
    next_nodes = nodes[actual_node]
    if next_direction == "L":
        next_node = next_nodes[0]
    else:
        next_node = next_nodes[1]
    #print(f" - Step {steps}, going from {actual_node} with direction {next_direction} to {next_node}")

    actual_node = next_node
    steps += 1


print(f"Solution {steps}")
