import re
file = open('16.txt', 'r')
lines = file.read().splitlines()


def print_release(valves):
    opened = []
    release = 0
    for valve, details in valves.items():
        if details["opened"]:
            opened.append(valve)
            release += details["rate"]
    if not opened:
        print("No valves are open")
    else:
        print("Vaves {} are open, releasing {} pressure".format(" and ".join(opened), release))


valves = {}
to_open = []
for line in lines:
    valve = re.findall("Valve (\D\D)", line)[0]
    rate = int(re.findall("rate=(\d*)", line)[0])
    if "valves" in line:
        leads = line.split("valves ")[1].split(", ")
    else:
        leads = line.split("valve ")[1].split(", ")
    print("valve {}, rate {} lead to valves {}".format(valve, rate, leads))
    valves[valve] = {
        "rate": rate,
        "opened": False,
        "leads": leads
    }
    if rate > 0:
        to_open.append(valve)
    # "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
#print(valves)
#print(valves["AA"]["leads"])
for valve, details in valves.items():
    targets = []
    for target_valve, target_details in valves.items():
        if target_valve != valve and target_details["rate"] > 0:
            targets.append(target_valve)
    walk = 0
    #print("targets for valve {} : {}".format(valve, targets))
    reachable = [valve]
    while targets:
        #print(reachable)
        walk += 1
        to_add = []
        to_remove = []
        for new_valve in reachable:
            to_add += valves[new_valve]["leads"]
            to_remove.append(new_valve)
        #print(to_add, to_remove)
        for item in to_remove:
            reachable.remove(item)
        reachable += to_add
        reachable = list(set(reachable))
        #print("Next reachable for walk {} : {}".format(walk, reachable))
        to_remove = []
        for target in targets:
            if target in reachable:
                details[target] = walk
                to_remove.append(target)
        for target in to_remove:
            targets.remove(target)
        #print("remaining targets {}".format(targets))
    #print("Final leads for valve {} : {}".format(valve, details))
print(valves)
current_valve = "AA"
total_time = 30
for minute in range(1, 31):
    print(" == Minute {} ==".format(minute))
    print_release(valves)
    best_release = 0
    print("current valve {}".format(valve))
    for test in to_open:
        time_to_reach = 0 if test == current_valve else valves[current_valve][test]
        total_release = (total_time - minute - time_to_reach - 1) * valves[test]["rate"]
        print(" - total release if targeting valve {} : {}".format(test, total_release))
