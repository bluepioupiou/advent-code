from utils import log

if __name__ == '__main__':
    file = open('1.txt', 'r')
    lines = file.readlines()
    position = 50
    nouvelle_position = position
    nombre_de_zero = 0
    for line in lines:
        log(f"Trouvé {line}")
        direction = line[0]
        decalage = int(line[1:])
        if direction == "R":
            nouvelle_position = position + decalage
        elif direction == "L":
            nouvelle_position = position - decalage

        nombre_de_zero += abs(nouvelle_position) // 100
        nouvelle_position = nouvelle_position % 100
        log(f" - on part de {position}, on va a {direction} de {decalage} pour arriver à {nouvelle_position}")
        if nouvelle_position == 0:
            nombre_de_zero += 1

        position = nouvelle_position
    log(f"{-21 % 100}")
    log(f"Fini ! nombre de zéro = {nombre_de_zero}")