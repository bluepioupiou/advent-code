from utils import log, Grid, Position, DIRECTIONS, INSTRUCTIONS
import re

file = open('16.txt', 'r')
lines = file.readlines()

total = 0

if __name__ == '__main__':
    grid = Grid(lines)
    starting_pos = grid.find("S")
    ending_pos = grid.find("E")
    paths = [[{"position": starting_pos, "direction": "RIGHT", "score": 0}]]
    final_paths = []
    while paths:
        log(f"{len(paths)} paths ending at : {[path[-1]['position'] for path in paths]}")
        path = paths.pop(0)
        tile = path[-1]
        position = tile["position"]
        neighbours = grid.neighbours(position)
        for neighbor in neighbours:
            if grid.at(neighbor) != "#" and (len(path) == 1 or neighbor != path[-2]["position"]):
                #log(f" - escape possible {neighbor}")
                new_path = path[:]
                new_direction = position.get_direction_to(neighbor)
                new_score = tile["score"]
                if new_direction == tile["direction"]:
                    new_score += 1
                else:
                    new_score += 1000
                new_tile = {"position": neighbor, "direction": new_direction, "score": new_score}
                new_path.append(new_tile)

                if grid.at(neighbor) == "E":
                    final_paths.append(new_path)
                    break
                for other_path in paths:
                    for other_tile in other_path:
                        if other_tile["position"] == new_tile["position"] and other_tile["direction"] == new_tile["direction"]:
                            log(f" - found same step between {new_path} and {other_path}")
                            if new_tile["score"] < other_tile["score"]:
                                log(f" - new path is better")
                                paths.remove(other_path)
                                paths.append(new_path)
                            break
                else:
                    log(f" - nothing alike, adding {new_path[-1]}")
                    paths.append(new_path)
        for path in paths:
            grid.replace(path[-1]["position"], INSTRUCTIONS[path[-1]["direction"]])
        print(grid)
        grid = Grid(lines)
    sorted(final_paths, key=lambda path: path[-1]["score"])

    log(final_paths)
    path = final_paths[0]
    for tile1, tile2 in zip(path[1:], path[2:]):
        grid.replace(tile1["position"], tile1["position"].get_instruction_to(tile2["position"]))
    print(grid)
    print(path[-1]["score"])