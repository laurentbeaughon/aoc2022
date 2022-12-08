from utils import read_integers_map


# visible = 2
# not visible = 1
# unknown = 0
# right, down, left, up
VISIBLE = {}


def is_visible(map, index, direction):
    ref = f"{index[0]}; {index[1]}"
    if VISIBLE.get(ref, [0, 0, 0, 0])[direction] == 2:
        return True
    elif VISIBLE.get(ref, [0, 0, 0, 0])[direction] == 1:
        return False

    if direction == 0:
        if index[1] == len(map[0]):
            answer = True
        else:
            answer = all(
                [
                    map[index[0]][index[1]] > map[index[0]][index[1] + i]
                    for i in range(1, len(map[0]) - index[1])
                ]
            )

    if direction == 1:
        if index[0] == len(map):
            answer = True
        else:
            answer = all(
                [
                    map[index[0]][index[1]] > map[index[0] + i][index[1]]
                    for i in range(1, len(map) - index[0])
                ]
            )

    if direction == 2:
        if index[1] == 0:
            answer = True
        else:
            answer = all(
                [
                    map[index[0]][index[1]] > map[index[0]][index[1] - i]
                    for i in range(1, index[1] + 1)
                ]
            )

    if direction == 3:
        if index[0] == 0:
            answer = True
        else:
            answer = all(
                [
                    map[index[0]][index[1]] > map[index[0] - i][index[1]]
                    for i in range(1, index[0] + 1)
                ]
            )

    if answer:
        VISIBLE[ref] = VISIBLE.get(ref, [0, 0, 0, 0])
        VISIBLE[ref][direction] = 2
        return True
    else:
        VISIBLE[ref] = VISIBLE.get(ref, [0, 0, 0, 0])
        VISIBLE[ref][direction] = 1
        return False


def part_1(map, verbose):
    directions = [0, 1, 2, 3]
    for i in range(len(map)):
        for j in range(len(map[0])):
            for direction in directions:
                is_visible(map, (i, j), direction)

    if verbose:
        print(VISIBLE)

    n_visible = sum([any(x == 2 for x in pos) for pos in VISIBLE.values()])

    return n_visible


def part_2(map, verbose):
    def vision(map, index):
        val = map[index[0]][index[1]]
        cpt = 1
        i = index[0]
        count = 0
        while i + 1 < len(map):
            if map[i + 1][index[1]] < val:
                count += 1
                i += 1
            else:
                count += 1
                i += len(map)
        cpt *= count
        count = 0

        i = index[0]
        while i > 0:
            if map[i - 1][index[1]] < val:
                count += 1
                i -= 1
            else:
                count += 1
                i -= len(map)
        cpt *= count
        count = 0

        i = index[1]
        while i + 1 < len(map[0]):
            if map[index[0]][i + 1] < val:
                count += 1
                i += 1
            else:
                count += 1
                i += len(map)
        cpt *= count
        count = 0

        i = index[1]
        while i > 0:
            if map[index[0]][i - 1] < val:
                count += 1
                i -= 1
            else:
                count += 1
                i -= len(map)
        cpt *= count
        return cpt

    max_view = 0
    max_index = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if vision(map, (i, j)) > max_view:
                max_view = vision(map, (i, j))
                max_index = (i, j)
    return max_view, max_index


def main(args):
    map = read_integers_map(args.data_file)
    print(part_1(map, args.verbose))
    print(part_2(map, args.verbose))
