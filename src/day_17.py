from tqdm import tqdm

from utils import read_raw_txt


def part_1(instructions, verbose):
    def insert_horizontal(map, top, state):
        s = 2
        t = 0
        while len(map) < top + 5:
            map.append([False for _ in range(7)])
        while True:
            instruction = instructions[state % len(instructions)]
            if instruction == "<" and s > 0 and not map[top + 4 - t][s - 1]:
                s -= 1
            elif instruction == ">" and s < 3 and not map[top + 4 - t][s + 4]:
                s += 1
            if (
                map[top + 3 - t][s]
                or map[top + 3 - t][s + 1]
                or map[top + 3 - t][s + 2]
                or map[top + 3 - t][s + 3]
            ):
                map[top + 4 - t] = [
                    s <= i <= s + 3 or map[top + 4 - t][i] for i in range(7)
                ]
                if top + 4 - t > top:
                    top = top + 4 - t
                return map, top, state + 1
            t += 1
            state += 1

    def insert_plus(map, top, state):
        s = 2
        t = 0
        while len(map) < top + 7:
            map.append([False for _ in range(7)])
        while True:
            instruction = instructions[state % len(instructions)]
            if (
                instruction == "<"
                and s > 0
                and not (
                    map[top + 5 - t][s - 1]
                    or map[top + 4 - t][s]
                    or map[top + 6 - t][s]
                )
            ):
                s -= 1
            elif (
                instruction == ">"
                and s < 4
                and not (
                    map[top + 5 - t][s + 3]
                    or map[top + 4 - t][s + 2]
                    or map[top + 6 - t][s + 2]
                )
            ):
                s += 1
            if (
                map[top + 4 - t][s]
                or map[top + 3 - t][s + 1]
                or map[top + 4 - t][s + 2]
            ):
                map[top + 4 - t] = [i == s + 1 or map[top + 4 - t][i] for i in range(7)]
                map[top + 5 - t] = [
                    s <= i <= s + 2 or map[top + 5 - t][i] for i in range(7)
                ]
                map[top + 6 - t] = [i == s + 1 or map[top + 6 - t][i] for i in range(7)]
                if top + 6 - t > top:
                    top = top + 6 - t
                return map, top, state + 1
            t += 1
            state += 1

    def insert_lshape(map, top, state):
        s = 2
        t = 0
        while len(map) < top + 7:
            map.append([False for _ in range(7)])
        while True:
            instruction = instructions[state % len(instructions)]
            if (
                instruction == "<"
                and s > 0
                and not (
                    map[top + 4 - t][s - 1]
                    or map[top + 5 - t][s + 1]
                    or map[top + 6 - t][s + 1]
                )
            ):
                s -= 1
            elif (
                instruction == ">"
                and s < 4
                and not (
                    map[top + 4 - t][s + 3]
                    or map[top + 5 - t][s + 3]
                    or map[top + 6 - t][s + 3]
                )
            ):
                s += 1
            if (
                map[top + 3 - t][s]
                or map[top + 3 - t][s + 1]
                or map[top + 3 - t][s + 2]
            ):
                map[top + 4 - t] = [
                    s <= i <= s + 2 or map[top + 4 - t][i] for i in range(7)
                ]
                map[top + 5 - t] = [i == s + 2 or map[top + 5 - t][i] for i in range(7)]
                map[top + 6 - t] = [i == s + 2 or map[top + 6 - t][i] for i in range(7)]
                if top + 6 - t > top:
                    top = top + 6 - t
                return map, top, state + 1
            t += 1
            state += 1

    def insert_vertical(map, top, state):
        s = 2
        t = 0
        while len(map) < top + 8:
            map.append([False for _ in range(7)])
        while True:
            instruction = instructions[state % len(instructions)]
            if (
                instruction == "<"
                and s > 0
                and not (
                    map[top + 4 - t][s - 1]
                    or map[top + 5 - t][s - 1]
                    or map[top + 6 - t][s - 1]
                    or map[top + 7 - t][s - 1]
                )
            ):
                s -= 1
            elif (
                instruction == ">"
                and s < 6
                and not (
                    map[top + 4 - t][s + 1]
                    or map[top + 5 - t][s + 1]
                    or map[top + 6 - t][s + 1]
                    or map[top + 7 - t][s + 1]
                )
            ):
                s += 1
            if map[top + 3 - t][s]:
                map[top + 4 - t] = [i == s or map[top + 4 - t][i] for i in range(7)]
                map[top + 5 - t] = [i == s or map[top + 5 - t][i] for i in range(7)]
                map[top + 6 - t] = [i == s or map[top + 6 - t][i] for i in range(7)]
                map[top + 7 - t] = [i == s or map[top + 7 - t][i] for i in range(7)]
                if top + 7 - t > top:
                    top = top + 7 - t
                return map, top, state + 1
            t += 1
            state += 1

    def insert_square(map, top, state):
        s = 2
        t = 0
        while len(map) < top + 6:
            map.append([False for _ in range(7)])
        while True:
            instruction = instructions[state % len(instructions)]
            if (
                instruction == "<"
                and s > 0
                and not (map[top + 4 - t][s - 1] or map[top + 5 - t][s - 1])
            ):
                s -= 1
            elif (
                instruction == ">"
                and s < 5
                and not (map[top + 4 - t][s + 2] or map[top + 5 - t][s + 2])
            ):
                s += 1
            if map[top + 3 - t][s] or map[top + 3 - t][s + 1]:
                map[top + 4 - t] = [
                    s <= i <= s + 1 or map[top + 4 - t][i] for i in range(7)
                ]
                map[top + 5 - t] = [
                    s <= i <= s + 1 or map[top + 5 - t][i] for i in range(7)
                ]
                if top + 5 - t > top:
                    top = top + 5 - t
                return map, top, state + 1
            t += 1
            state += 1

    map = [[1 for _ in range(7)]]
    map += [[False for _ in range(7)] for _ in range(4)]
    top = 0
    state = 0
    for i in tqdm(range(6880)):  # 2672
        if i % 5 == 0:
            map, top, state = insert_horizontal(map, top, state)
        if i % 5 == 1:
            map, top, state = insert_plus(map, top, state)
        if i % 5 == 2:
            map, top, state = insert_lshape(map, top, state)
        if i % 5 == 3:
            map, top, state = insert_vertical(map, top, state)
        if i % 5 == 4:
            map, top, state = insert_square(map, top, state)
    if verbose:
        for i in range(len(map)):
            print("".join("X" if x else " " for x in map[-i - 1]))
    return top


def main(args):
    instructions = read_raw_txt(args.data_file)
    print(part_1(instructions, args.verbose))
