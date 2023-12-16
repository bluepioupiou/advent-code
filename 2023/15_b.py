
if __name__ == '__main__':
    total = 0
    boxes = {}
    file = open('15'
                '.txt', 'r')
    lines = file.readlines()

    data = lines[0].strip().split(",")
    print(data)
    for step in data:
        if step.count("-"):
            label = step[:-1]
            focal = None
        else:
            label, focal = step.split("=")
        print(f"label {label}, focal {focal}")

        current_value = 0
        for c in label:
            current_value = ((current_value + ord(c)) * 17) % 256

        print(f"{label} become {current_value}")
        if focal:
            if current_value not in boxes:
                boxes[current_value] = []
            for rank, lens in enumerate(boxes[current_value]):
                if label in lens:
                    print(f"Remplace {lens} with new {label} {focal}")
                    boxes[current_value][rank] = f"{label} {focal}"
                    break
            else:
                print(f"Adding new {label} {focal}")
                boxes[current_value].append(f"{label} {focal}")
        else:
            if current_value in boxes:
                for rank, lens in enumerate(boxes[current_value]):
                    if label in lens:
                        print(f"Deleting {label} {focal} at rank")
                        del boxes[current_value][rank]
    print(boxes)
    total = 0
    for box_number, box in boxes.items():
        for slot_number, slot in enumerate(box, 1):
            label, focal = slot.split(" ")
            power = (box_number + 1) * slot_number * int(focal)
            print(f"{label}: {(box_number + 1)} (box {box_number}) * {(slot_number - 1)} (slot {slot_number}) * {focal} (focal length) = {power}")
            total += power
    print(total)