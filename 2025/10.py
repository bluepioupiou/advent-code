import re
from utils import log

if __name__ == '__main__':
    file = open('10.txt', 'r')
    lines = file.readlines()
    result = 0
    for line in lines:
        target_light = re.search(r"\[(.*?)\]", line).group(1)
        buttons = [tuple(map(int, x.split(","))) for x in re.findall(r"\((.*?)\)", line)]
        #joltage = re.search(r"\{(.*?)\}", line).group(1)
        log(f"lights {target_light}, buttons {buttons}")
        current_lights = [".".join("" for position in target_light) + "."]
        iteration = 0
        while True:
            new_lights = []
            iteration += 1
            for initial_current_light in current_lights:
                for button in buttons:
                    current_light = initial_current_light
                    for position in button:
                        current_light = current_light[:position] + ("#" if current_light[position] == "." else ".") + current_light[position + 1:]
                    #log(f" - with button {button}: {initial_current_light} > {current_light}")
                    if current_light == target_light:
                        # On a trouvé !
                        log(f"at iteration {iteration}: found {current_light} from {initial_current_light} with button {button}")
                        break
                    new_lights.append(current_light)
                else:
                    continue
                break
            else:
                current_lights = new_lights
                #log(f"at iteration {iteration}: {current_lights}")
                continue
            #log(f"found min iteration {iteration}")
            result += iteration
            break


    print(result)

