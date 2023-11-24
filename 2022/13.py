import json
file = open('13.txt', 'r')
lines = file.read().splitlines()

cycle = 1
total = 0


def compare_objects(left_element, right_element, nested):
    print("{}- Compare {} and {}".format("  " * nested, left_element, right_element))
    if isinstance(left_element, list) and isinstance(right_element, list):
        for left_child, right_child in zip(left_element, right_element):
            compare = compare_objects(left_child, right_child, nested + 1)
            if compare is not None:
                return compare
        else:
            nested += 1
            if len(left_element) > len(right_element):
                print("{}- Right side ran out of items, so inputs are not in the right order".format("  " * nested))
                return False
            elif len(left_element) < len(right_element):
                print("{}- Left side ran out of items, so inputs are in the right order".format("  " * nested))
                return True
    elif isinstance(left_element, int) and isinstance(right_element, int):
        nested += 1
        if right_element < left_element:
            print("{}- Right side is smaller, so inputs are not in the right order".format("  " * nested))
            return False
        elif left_element < right_element:
            print("{}- Left side is smaller, so inputs are in the right order".format("  " * nested))
            return True
    else:
        nested += 1
        if isinstance(left_element, int):
            left_element = [left_element]
            print("{}- Mixed types; convert left to {} and retry comparison".format("  " * nested, left_element))
        else:
            right_element = [right_element]
            print("{}- Mixed types; convert right to {} and retry comparison".format("  " * nested, right_element))
        return compare_objects(left_element, right_element, nested)
    return None


for left, right in zip(lines[0::3], lines[1::3]):
    print("== Pair {} ==".format(cycle))
    compare = compare_objects(json.loads(left), json.loads(right), 0)
    print(compare)
    if compare:
        total += cycle
    cycle += 1
print("total = {}".format(total))

