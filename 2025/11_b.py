import re
from utils import log
from collections import defaultdict, deque

def count_paths_from_end(graph, start, end):
    # Comptage du nombre de dépendances sortantes
    out_degree = defaultdict(int)
    for node, children in graph.items():
        out_degree[node] = len(children)
        for child in children:
            out_degree.setdefault(child, 0)

    # Initialisation des chemins
    paths = defaultdict(int)
    paths[end] = 1

    # File des nœuds "résolus" (sans sorties)
    queue = deque(node for node, deg in out_degree.items() if deg == 0)

    while queue:
        node = queue.popleft()

        # Pour chaque parent implicite
        for parent, children in graph.items():
            if node in children:
                paths[parent] += paths[node]
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)

    return paths[start]
if __name__ == '__main__':
    file = open('11.txt', 'r')
    lines = file.readlines()
    result = 0
    paths = {}

    for line in lines:
        key, value = line.split(":")
        paths[key.strip()] = value.strip().split()


    log(paths)
    svr_to_fft = count_paths_from_end(paths, 'svr', 'fft')
    log(f"Paths to fft: {svr_to_fft}")

    fft_to_dac = count_paths_from_end(paths, 'fft', 'dac')
    log(f"Paths to dac: {fft_to_dac}")

    dac_to_out = count_paths_from_end(paths, 'dac', 'out')
    log(f"Paths to out: {dac_to_out}")

    print(svr_to_fft * fft_to_dac * dac_to_out)

