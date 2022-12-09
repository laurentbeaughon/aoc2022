from utils import read_movements


def part_1(movements, verbose):
    tail_positions = {"0 0"}
    head_pos = (0, 0)
    tail_pos = (0, 0)
    direction = {
        "R": [0, 1],
        "L": [0, -1],
        "D": [1, 0],
        "U": [-1, 0],
    }
    for move in movements:
        for _ in range(move[1]):
            new_pos = [sum(x) for x in zip(head_pos, direction[move[0]])]
            if abs(new_pos[0] - tail_pos[0]) > 1 or abs(new_pos[1] - tail_pos[1]) > 1:
                tail_positions.add(f"{head_pos[0]} {head_pos[1]}")
                tail_pos = head_pos
            head_pos = new_pos

    return len(tail_positions)


def part_2(movements, verbose):
    def catch_up(pos1, pos2):
        out_0, out_1 = pos1
        if abs(pos1[0] - pos2[0]) == 2:
            out_0 = int((pos1[0] + pos2[0]) / 2)
            if abs(pos1[1] - pos2[1]) == 1:
                out_1 = pos2[1]
        if abs(pos1[1] - pos2[1]) == 2:
            out_1 = int((pos1[1] + pos2[1]) / 2)
            if abs(pos1[0] - pos2[0]) == 1:
                out_0 = pos2[0]
        return (out_0, out_1)

    def print_map(pos):
        max_w = max(max(x[1] for x in pos), 0)
        min_w = min(min(x[1] for x in pos), 0)
        max_h = max(max(x[0] for x in pos), 0)
        min_h = min(min(x[0] for x in pos), 0)
        map = [["-"] * (1 + max_w - min_w) for i in range((1 + max_h - min_h))]

        map[pos[0][0] - min_h][pos[0][1] - min_w] = "H"
        map[-min_h][-min_w] = "S"
        for i in range(1, 10):
            map[pos[i][0] - min_h][pos[i][1] - min_w] = str(i)

        print("\n".join(["".join(x) for x in map]))
        print()

    tail_positions = {"0 0"}
    rope_pos = [(0, 0)] * 10
    direction = {
        "R": [0, 1],
        "L": [0, -1],
        "D": [1, 0],
        "U": [-1, 0],
    }
    for move in movements:
        if verbose:
            print(move)
        for _ in range(move[1]):
            new_pos = [tuple(sum(x) for x in zip(rope_pos[0], direction[move[0]]))] + [
                (0, 0)
            ] * 9
            for i in range(1, 10):
                new_pos[i] = catch_up(rope_pos[i], new_pos[i - 1])
            rope_pos = new_pos
            tail_positions.add(f"{rope_pos[-1][0]} {rope_pos[-1][1]}")
        if verbose:
            print_map(rope_pos)
    return len(tail_positions)


def main(args):
    movements = read_movements(args.data_file)
    print(part_1(movements, args.verbose))
    print(part_2(movements, args.verbose))
