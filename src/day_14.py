from utils import read_rock_structures


def draw_map(structures):
    max_x = max([max([x[0] for x in sequence]) for sequence in structures])
    min_x = min([min([x[0] for x in sequence]) for sequence in structures])
    max_y = max([max([x[1] for x in sequence]) for sequence in structures])
    map = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]

    for sequence in structures:
        pos = sequence[0]
        map[pos[1]][pos[0] - min_x] = 1
        for pair in sequence[1:]:
            if pair[0] == pos[0]:
                for i in range(pair[1] - pos[1]):
                    map[pos[1] + i + 1][pos[0] - min_x] = 1
                for i in range(pos[1] - pair[1]):
                    map[pos[1] - i - 1][pos[0] - min_x] = 1
            else:
                for i in range(pair[0] - pos[0]):
                    map[pos[1]][pos[0] + i + 1 - min_x] = 1
                for i in range(pos[0] - pair[0]):
                    map[pos[1]][pos[0] - i - 1 - min_x] = 1
            pos = pair
    return map, 500 - min_x


def insert_sand(map, insert_pos):
    y = 0
    x = insert_pos
    while True:
        if y == len(map) - 1:
            return False
        if x == 0:
            if not map[y + 1][x]:
                y += 1
            else:
                return False
        elif x == len(map[0]) - 1:
            if not map[y + 1][x]:
                y += 1
            elif not map[y + 1][x - 1]:
                y += 1
                x -= 1
            else:
                return False
        else:
            if not map[y + 1][x]:
                y += 1
            elif not map[y + 1][x - 1]:
                y += 1
                x -= 1
            elif not map[y + 1][x + 1]:
                y += 1
                x += 1
            else:
                map[y][x] = 2
                return True


def display(map):
    for line in map:
        print("".join([" " if x == 0 else "█" if x == 1 else "O" for x in line]))


def part_1(structures, verbose):
    map, insert_pos = draw_map(structures)
    if verbose:
        display(map)
    i = 0
    while insert_sand(map, insert_pos):
        i += 1
    if verbose:
        display(map)
    return i


def part_2(structures, verbose):
    map, insert_pos = draw_map(structures)
    insert_pos += len(map)
    map = [
        [0 for _ in range(len(map))] + line + [0 for _ in range(len(map))]
        for line in map
    ]
    map = map + [[0 for _ in range(len(map[0]))], [1 for _ in range(len(map[0]))]]
    i = 0
    while map[0][insert_pos] == 0:
        insert_sand(map, insert_pos)
        i += 1
    if verbose:
        if (length := len(map[0])) > 200:
            print(length)
            display([line[length // 2 - 100 : length // 2 + 100] for line in map])
        else:
            display(map)
    return i


def main(args):
    structures = read_rock_structures(args.data_file)
    print(part_1(structures, args.verbose))
    print(part_2(structures, args.verbose))
