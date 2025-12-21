from utils import log

if __name__ == '__main__':
    file = open('6.txt', 'r')
    lines = file.readlines()
    result = 0
    operand = None
    sub_result = 0
    for position, char in enumerate(lines[-1]):
        #log(f"char {char} at position {position}")
        if not char == " ":
            if sub_result:
                print(f" = {sub_result}")
                result += sub_result
            operand = char
            log(f"Operand {operand}")
            if operand == "*":
                sub_result = 1
            elif operand == "+":
                sub_result = 0
        number = ("".join(line[position] for line in lines[:-1])).strip()
        #log(number)
        if number:
            if operand == "*":
                log(f"* {number}")
                sub_result *= int(number)
            elif operand == "+":
                log(f"+ {number}")
                sub_result += int(number)

    result += sub_result
    print(result)
