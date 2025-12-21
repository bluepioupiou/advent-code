from utils import log

if __name__ == '__main__':
    file = open('6.txt', 'r')
    lines = file.readlines()
    result = 0
    calculs = []
    for line in lines:
        line = line.strip().split()
        calculs.append(line)
    for col in range(0,len(calculs[0])):
        operand = calculs[-1][col]
        print(f"operand: {operand}")
        for row in range(0, len(calculs[:-1])):
            log(f" {operand} {calculs[row][col]}")
            if operand == "*":
                if row == 0:
                    col_result = 1
                col_result *= int(calculs[row][col])
            elif operand == "+":
                if row == 0:
                    col_result = 0
                col_result += int(calculs[row][col])
        print(f" = {col_result}")
        result += col_result
    print(f" résultat final : {result}")
