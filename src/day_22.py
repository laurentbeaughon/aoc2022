from tqdm import tqdm
from utils import read_map_and_path


def prepare_map(map):
    row_inner_wall = [
        [i for i in range(len(map[j])) if map[j][i] == 1]
        for j in range(len(map))
    ]
    column_inner_wall = [
        [j for j in range(len(map)) if map[j][i] == 1]
        for i in range(len(map[0]))
    ]
    column_tunnel = []
    row_tunnel = []
    for i in range(len(map)):
        start = 0
        j = 0
        while map[i][j] == -1:
            start += 1
            j += 1
        while j < len(map[i]) and map[i][j] != -1:
            j += 1
        end = j
        row_tunnel.append((start, end))
    for j in range(len(map[0])):
        start = 0
        i = 0
        while map[i][j] == -1:
            start += 1
            i += 1
        while i < len(map) and map[i][j] != -1:
            i += 1
        end = i
        column_tunnel.append((start, end))

    prepared_map = {
        "column_walls": column_inner_wall,
        "row_walls": row_inner_wall,
        "column_tunnel": column_tunnel,
        "row_tunnel": row_tunnel,
    }
    return prepared_map


def hit_wall(start, length, walls, tunnel, dir):
    end = start + length * dir
    for wall in walls[::dir]:
        if dir * start < dir * wall <= dir * end:
            return wall - 1 * dir
    if end >= tunnel[1]:
        end = end - tunnel[1] + tunnel[0]
        if walls and walls[0] <= end:
            return walls[0] - 1 if walls[0] > tunnel[0] else tunnel[1] - 1
    if end < tunnel[0]:
        end = end - tunnel[0] + tunnel[1] 
        if  walls and walls[-1] >= end:
            return walls[-1] + 1 if walls[-1] < tunnel[1] - 1 else tunnel[0]
    return end


def part_1(map, path, verbose):
    print(path)
    def move(position, length, direction):
        nx, ny = position
        if direction == 0:
            line_wall = map["row_walls"][position[0]]
            line_tunnel = map["row_tunnel"][position[0]]
            ny = hit_wall(position[1], length, line_wall, line_tunnel, 1)
        elif direction == 1:
            line_wall = map["column_walls"][position[1]]
            line_tunnel = map["column_tunnel"][position[1]]
            nx = hit_wall(position[0], length, line_wall, line_tunnel, 1)
        elif direction == 2:
            line_wall = map["row_walls"][position[0]]
            line_tunnel = map["row_tunnel"][position[0]]
            ny = hit_wall(position[1], length, line_wall, line_tunnel, -1)
        elif direction == 3:
            line_wall = map["column_walls"][position[1]]
            line_tunnel = map["column_tunnel"][position[1]]
            nx = hit_wall(position[0], length, line_wall, line_tunnel, -1)
        return (nx, ny)

    pos = (0, map["row_tunnel"][0][0])
    for x, direction in path:
        print(f"direction: {direction}")
        pos = move(pos, x, direction)
        print(f"new pos {pos}")
        print()
    return (pos[0]+1)*1000 + (pos[1]+1)*4 + direction

    
def part_2(map, path, verbose):
    # unfun problem, too lazy to do it. I might come back later
    return


def main(args):
    map, path = read_map_and_path(args.data_file)
    for line in map:
        print("".join([" " if char == 0 else "#" for char in line]))
    map = prepare_map(map)
    print(map)
    print(part_1(map, path, args.verbose))
    print(part_2(map, path, args.verbose))
