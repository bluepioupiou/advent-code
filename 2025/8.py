from utils import log, Grid, DIRECTIONS
import math
import itertools

if __name__ == '__main__':
    file = open('8.txt', 'r')
    lines = file.readlines()
    boxes = [(int(x[0]), int(x[1]), int(x[2])) for x in [line.strip().split(",") for line in lines]]
    log(boxes)
    distances = {}
    for first in boxes:
        for second in boxes:
            distance = math.sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2 + (first[2] - second[2])**2)
            if distance:
                distances[distance] = [first, second]
    distances = sorted(distances.items())
    log(distances)
    circuits = []
    connections = 0
    for connection in range(0, 10):
        shortest = distances.pop(0)
        log(f"connecting together {shortest[1]}")
        for circuit in circuits:
            found = False
            if shortest[1][0] in circuit and shortest[1][1] in circuit:
                log(f" - already in a circuit, nothing happen")
                break
            if shortest[1][0] in circuit:
                circuit.append(shortest[1][1])
                found = True
            elif shortest[1][1] in circuit:
                circuit.insert(0, shortest[1][0])
                found = True

            if found:
                log(f" - adding to circuit to get {circuit}")
                break
        else:
            log(f" - new sub circuit")
            circuits.append(shortest[1])

        for circuit1, circuit2 in itertools.combinations(circuits, 2):
            if any(map(lambda v: v in circuit1, circuit2)):
                new_circuit = list(set(circuit1 + circuit2))
                log(f" # new circuit {new_circuit} from {circuit1} and {circuit2}")
                circuits.remove(circuit1)
                circuits.remove(circuit2)
                circuits.append(new_circuit)
        log(f" --> {circuits}")

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    log(" * ".join([str(len(circuit)) for circuit in circuits][:3]))
    print(math.prod([len(circuit) for circuit in circuits][:3]))
