import re
from utils import log

def count_paths(graph, start, end):
    def dfs(node, visited):
        # Si on atteint la destination, on a trouvé un chemin
        if node == end:
            return 1

        # Si le nœud n’a pas de sorties, aucun chemin
        if node not in graph:
            return 0

        total = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                total += dfs(neighbor, visited | {neighbor})
        return total

    return dfs(start, {start})

if __name__ == '__main__':
    file = open('11.txt', 'r')
    lines = file.readlines()
    result = 0
    paths = {}

    for line in lines:
        key, value = line.split(":")
        paths[key.strip()] = value.strip().split()


    log(paths)
    print(count_paths(paths, 'you', 'out'))

