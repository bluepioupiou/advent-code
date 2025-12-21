import re
from utils import log
from z3 import *

if __name__ == '__main__':
    file = open('10.txt', 'r')
    lines = file.readlines()
    result = 0
    for line in lines:
        target_light = re.search(r"\[(.*?)\]", line).group(1)
        buttons = [list(map(int, x.split(",")))
           for x in re.findall(r"\((.*?)\)", line)]
        vectors = []
        for button in buttons:
            #log(f" - build button {button} for len {len(target_light)}")
            vectors.append([1 if i in button else 0 for i in range(len(target_light))])
        target_voltage = [int(x) for x in re.search(r"\{(.*?)\}", line).group(1).split(",")]
        #log(f"target_light {target_light}, vectors {vectors}, target_voltages {target_voltage}({len(target_voltage)})")

        s = Solver()
        x = [Int(f"x_{i}") for i in range(len(vectors))]

        for i in range(len(vectors)):
            s.add(x[i] >= 0)

        for j in range(len(target_voltage)):
            s.add(
                Sum([x[i] * vectors[i][j] for i in range(len(vectors))]) == target_voltage[j]
            )

        opt = Optimize()
        opt.add(s.assertions())
        opt.minimize(Sum(x))

        if opt.check() == sat:
            m = opt.model()
            result += sum([m[x[i]].as_long() for i in range(len(vectors))])
    print(result)

