import re
from utils import log

def rotate_shape(cells):
    """
    cells: set of (x,y)
    returns: list of sets, each set = rotation normalisée de la forme
             [90°, 180°, 270°]
    """
    rotations = [cells]

    # Transform set -> list of tuples
    coords = list(cells)

    for k in [1,2,3]:  # 90,180,270
        if k == 1:
            # 90°: (x,y) -> (-y, x)
            rot = [(-y, x) for x,y in coords]
        elif k == 2:
            # 180°: (x,y) -> (-x, -y)
            rot = [(-x, -y) for x,y in coords]
        elif k == 3:
            # 270°: (x,y) -> (y, -x)
            rot = [(y, -x) for x,y in coords]

        # Normalisation : coin haut-gauche à (0,0)
        minx = min(x for x,y in rot)
        miny = min(y for x,y in rot)
        norm = [(x - minx, y - miny) for x,y in rot]

        rotations.append(norm)

    return rotations
def flip_shape(cells):
    """
    cells: set of (x, y)
    Returns: normalized flipped set
    """
    # coordonnées originales
    xs = [x for x, y in cells]

    maxx = max(xs)

    flipped = set()
    for x, y in cells:
        new_x = maxx - x
        new_y = y
        flipped.add((new_x, new_y))

    # normalisation (coin haut-gauche à 0,0)
    minx = min(x for x, y in flipped)
    miny = min(y for x, y in flipped)
    normalized = [(x - minx, y - miny) for x, y in flipped]

    return normalized

def cells_to_offsets(cells, W):
    return [y * W + x for x, y in cells]

def deduplicate(cells_list):
    unique_cells = list({frozenset(f) for f in cells_list})
    return [list(s) for s in unique_cells]

def print_grid(grid, W, H):
    for y in range(H):
        row = grid[y*W:(y+1)*W]
        log("".join("#" if v > 0 else "." for v in row))
    log("\n")

def all_translations(grid, offsets, W, H):
    xs = [o % W for o in offsets]
    ys = [o // W for o in offsets]
    max_x = max(xs)
    max_y = max(ys)

    for base in (
        y * W + x
        for y in range(H - max_y)
        for x in range(W - max_x)
    ):
        new_grid = grid.copy()
        for o in offsets:
            new_grid[base + o] += 1
        yield new_grid

def apply_cells(grid, cells):
    new_grid = grid.copy()
    for i in cells:
        new_grid[i] += 1
    return new_grid

def find_if_fit(grid, blocks_as_cells_for_grid):
    grids = [grid]
    for form_number, form_all_cells in enumerate(blocks_as_cells_for_grid):
        # Si il n'y a plus de grid possible résultant à cette étape, c'est que c'est déjà mort
        if not grids:
            return False
        # Si on a moins de cellule vide dispos à cette étape qu'il n'y a de case dans la prochaine forme, c'est mort
        if grid.count(0) < len(form_all_cells[0]):
            return False
        log(f"- for form number: {form_number}, grids = {len(grids)}")
        new_grids = set()
        for current_grid in grids:
            for cells in form_all_cells:
                for translation in all_translations(current_grid, cells, width, height):
                    if not 2 in translation:
                        if form_number == len(blocks_as_cells_for_grid) - 1:
                            # On vient de faire rentrer la dernière form, pas besoin d'aller plus loin
                            return True
                        new_grids.add(tuple(translation))
        grids = [list(row) for row in {row for row in new_grids}]
                        # print_grid(translation, width, height)
    # On a pas trouvé et tout parcouru, normalement on passe jamais par là mais on retourne False
    return False

if __name__ == '__main__':
    file = open('12.txt', 'r')
    result = 0

    blocks = re.split(r"\n\s*\n", file.read())

    blocks_as_shapes = {}
    blocks_as_cells = []
    for block in blocks[:-1]:
        lines = block.splitlines()
        idx = int(lines[0].rstrip(":"))
        shape = lines[1:]
        blocks_as_shapes[idx] = shape

        cells = [
            (x, y)
            for y, row in enumerate(shape)
            for x, c in enumerate(row)
            if c == '#'
        ]
        blocks_as_cells.append(cells)

    log(f"shapes: {blocks_as_shapes}")
    log(f"blocks_as_cells: {blocks_as_cells}")

    for line in blocks[-1].splitlines():
        log(line)
        if 'x' in line:
            integers = list(map(int, re.findall(r"\d+", line.strip())))
            log(f"- integers: {integers}")
            # préparation du grid
            width = integers[0]
            height = integers[1]
            grid = [0] * (width * height)
            # On ne garde que les formes sélectionnées
            selected_forms = []
            for i, integer in enumerate(integers[2:]):
                for j in range(integer):
                    selected_forms.append(blocks_as_cells[i])
            log(f"- selected_forms: {selected_forms}")
            # ajout de toutes les rotations et miroirs, dédoublonnées
            rotated_and_flipped = [deduplicate(rotate_shape(selected_form) + rotate_shape(flip_shape(selected_form))) for selected_form in selected_forms]
            log(f"- rotated_and_flipped: {rotated_and_flipped}")
            # préparation des form adaptées au grid
            blocks_as_cells_for_grid = [[cells_to_offsets(f, width) for f in group] for group in rotated_and_flipped]
            log(f"- blocks_as_cells_for_grid: {blocks_as_cells_for_grid}")
            if find_if_fit(grid, blocks_as_cells_for_grid):
                result += 1



    print(result)

