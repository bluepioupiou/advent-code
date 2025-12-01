from utils import log, Grid, Position, DIRECTIONS, INSTRUCTIONS
import re

file = open('17.txt', 'r')
lines = file.readlines()

total = 0
pointer = 0

OPCODE_ADV = 0
OPCODE_BXL = 1
OPCODE_BST = 2
OPCODE_JNZ = 3
OPCODE_BXC = 4
OPCODE_OUT = 5
OPCODE_BDV = 6
OPCODE_CDV = 7

if __name__ == '__main__':
    index = 0
    program = [int(x) for x in lines[4].split(": ")[1].split(",")]
    while True:
        index += 1
        registerA = int(lines[0].split(": ")[1]) + index
        registerB = int(lines[1].split(": ")[1])
        registerC = int(lines[2].split(": ")[1])
        pointer = 0
        output = []
           print(f"Trying {registerA} {registerB} {registerC}")
        while True:
            if pointer >= len(program):
                break
            jump = False
            opcode = program[pointer]
            literal_operand = program[pointer + 1]
            if literal_operand == 4:
                combo_operand = registerA
            elif literal_operand == 5:
                combo_operand = registerB
            elif literal_operand == 6:
                combo_operand = registerC
            else:
                combo_operand = literal_operand

            if opcode == OPCODE_ADV:
                registerA = registerA // (2 ** combo_operand)
            elif opcode == OPCODE_BXL:
                registerB = registerB ^ literal_operand
            elif opcode == OPCODE_BST:
                registerB = combo_operand % 8
            elif opcode == OPCODE_JNZ:
                if registerA != 0:
                    jump = True
                    pointer = literal_operand
            elif opcode == OPCODE_BXC:
                registerB = registerB ^ registerC
            elif opcode == OPCODE_OUT:
                output.append(combo_operand % 8)
            elif opcode == OPCODE_BDV:
                registerB = registerA // (2 ** combo_operand)
            elif opcode == OPCODE_CDV:
                registerC = registerA // (2 ** combo_operand)

            if not jump:
                pointer += 2
        print("- " + ",".join([str(value) for value in output]))
        if output == program:
            break
    print(initial_registerA)
