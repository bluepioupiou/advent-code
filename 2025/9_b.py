from utils import log, Grid, Position, DIRECTIONS
import math
import itertools

if __name__ == '__main__':
    file = open('9.txt', 'r')
    lines = file.readlines()
    corners = [Position(int(x[1]), int(x[0])) for x in [line.strip().split(",") for line in lines]]
    max_col = max(corners, key=lambda corner: corner.col).col + 1
    log(f"max_width :{max_col}, corners: {corners}")
    distances = {}
    for corner1, corner2 in itertools.combinations(corners, 2):
        distance = abs(corner1.row - corner2.row) + abs(corner1.col - corner2.col)
        if distance not in distances:
            distances[distance] = []
        distances[distance].append([corner1, corner2])
    distances = sorted(distances.items(), reverse=True)
    log(f"distances: {distances}")
    # On calcule les colonnes verticales avec [colonne, début de la ligne, fin de la ligne]
    walls = []
    for corner1, corner2 in zip(corners, corners[1:] + [corners[0]]):
        if corner1.col == corner2.col:
            walls.append([corner1.col, min(corner1.row, corner2.row), max(corner1.row, corner2.row)])
    log(f"walls: {walls}")

    best_area = 0
    # On prend les paires de coins par deux pour tester le rectangle
    for distance, corners_couples in distances:
        for corner1, corner2 in corners_couples:
            log(f"testing distance {distance} for {corner1} and {corner2}")
            # On anticipe les deux angles restants pour tester si ils sont dedans
            for shadow_corner in [Position(corner1.row, corner2.col), Position(corner2.row, corner1.col)]:
                #log(f" - looking for shadow_corner {shadow_corner}")
                if shadow_corner in corners:
                    #log(f"   - already a corner")
                    continue
                inside = False
                for col in range(shadow_corner.col, max_col):
                    # On fait du ray tracing =
                    # - si on croise un nombre pair de mur = on est à l'extérieur
                    # - Si on croise un nombre impair de murs = on est à l'intérieur
                    inline_walls = list(filter(lambda wall: wall[0] == col, walls))
                    #log(f"   - walls on col {col}: {inline_walls}")
                    if not inline_walls:
                        # On croise pas de murs sur cette colonne, on peut continuer d'avancer
                        continue
                    for wall in inline_walls:
                        if shadow_corner.row in range(wall[1], wall[2]):
                            #log(f"   - new wall encountered on {shadow_corner.row}:{col} = {(wall[1], wall[2])}")
                            inside = not inside
                if not inside:
                    #log(f"   - {shadow_corner} is outside ><")
                    break
            # On a pas fait de break = aucun des autres angles est à l'extérieur
            else:
                area = (abs(corner1.row - corner2.row) + 1) * (abs(corner1.col - corner2.col) + 1)
                log(f"  --> area for {corner1} and {corner2} is {area}")
                best_area = max(best_area, area)

        else:
            continue
        break
        #log("")
    print(best_area)
