import re
from utils import log

if __name__ == '__main__':
    file = open('10.txt', 'r')
    lines = file.readlines()
    result = 0
    for line in lines:
        target_light = re.search(r"\[(.*?)\]", line).group(1)
        buttons = [tuple(map(int, x.split(","))) for x in re.findall(r"\((.*?)\)", line)]
        target_voltage = tuple(int(x) for x in re.search(r"\{(.*?)\}", line).group(1).split(","))
        log(f"target_light {target_light}, buttons {buttons}, target_voltages {target_voltage}({len(target_voltage)})")
        current_voltages = {tuple([0] * len(target_voltage))}
        log(f"starting voltages {current_voltages}")
        iteration = 0
        while True:
            new_voltages = set()
            iteration += 1
            for initial_current_voltage in current_voltages:
                for button in buttons:
                    current_voltage = initial_current_voltage
                    for position in button:
                        current_voltage = (*current_voltage[:position], current_voltage[position] + 1, *current_voltage[position + 1:])
                    #log(f" - with button {button}: {initial_current_voltage} > {current_voltage} ... {target_voltage}")
                    if current_voltage == target_voltage:
                        # On a trouvé !
                        log(f"at iteration {iteration}: found {current_voltage} from {initial_current_voltage} with button {button}")
                        break
                    new_voltages.add(current_voltage)
                else:
                    continue
                break
            else:
                current_voltages = new_voltages
                log(f"at iteration {iteration}: {len(current_voltages)}")
                continue
            #log(f"found min iteration {iteration}")
            result += iteration
            break

    print(result)

