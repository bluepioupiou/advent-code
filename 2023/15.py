
if __name__ == '__main__':
    total = 0
    file = open('15'
                '.txt', 'r')
    lines = file.readlines()

    data = lines[0].strip().split(",")
    print(data)
    for step in data:
        current_value = 0
        for c in step:
            current_value = ((current_value + ord(c)) * 17) % 256
        total += current_value
        print(f"{step} become {current_value}")
    print(f"Total {total}")