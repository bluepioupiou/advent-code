import json
file = open('13.txt', 'r')
lines = file.read().splitlines()


def compare_objects(left_element, right_element, nested):
    #print("{}- Compare {} and {}".format("  " * nested, left_element, right_element))
    if isinstance(left_element, list) and isinstance(right_element, list):
        for left_child, right_child in zip(left_element, right_element):
            compare = compare_objects(left_child, right_child, nested + 1)
            if compare is not None:
                return compare
        else:
            if len(left_element) > len(right_element):
                #print("{}- Right side ran out of items, so inputs are not in the right order".format("  " * nested))
                return False
            elif len(left_element) < len(right_element):
                #print("{}- Left side ran out of items, so inputs are in the right order".format("  " * nested))
                return True
    elif isinstance(left_element, int) and isinstance(right_element, int):
        if right_element < left_element:
            #print("{}- Right side is smaller, so inputs are not in the right order".format("  " * nested))
            return False
        elif left_element < right_element:
            #print("{}- Left side is smaller, so inputs are in the right order".format("  " * nested))
            return True
    else:
        if isinstance(left_element, int):
            left_element = [left_element]
            #print("{}- Mixed types; convert left to {} and retry comparison".format("  " * nested, left_element))
        else:
            right_element = [right_element]
            #print("{}- Mixed types; convert right to {} and retry comparison".format("  " * nested, right_element))
        return compare_objects(left_element, right_element, nested + 1)
    return None


packets = []
for left, right in zip(lines[0::3], lines[1::3]):
    packets.append(json.loads(left))
    packets.append(json.loads(right))

packets.append(json.loads("[[2]]"))
packets.append(json.loads("[[6]]"))

for packet in packets:
    print(packet)

passages = 0
while True:
    passages += 1
    for pos in range(len(packets) - 1):
        left = packets[pos]
        right = packets[pos + 1]
        if not compare_objects(left, right, 0):
            packets[pos] = right
            packets[pos + 1] = left
            break
    else:
        break

print(" == Solution == ")
print("En {} passages".format(passages))
two = None
six = None
for count, packet in enumerate(packets, 1):
    if packet == json.loads("[[2]]"):
        two = count
    elif packet == json.loads("[[6]]"):
        six = count
    print(packet)

print(two * six)

