import sys

sys.setrecursionlimit(5000)

from utils import read_strings


def shortest_path(i, j, map, memoization, end):
    if map[i][j] == end:
        return memoization[i][j]
    length = memoization[i][j] + 1
    lengths = []

    if (
        i > 0
        and map[i - 1][j] - map[i][j] <= 1
        and (memoization[i - 1][j] is None or length < memoization[i - 1][j])
    ):
        memoization[i - 1][j] = length
        lengths.append(shortest_path(i - 1, j, map, memoization, end))

    if (
        j > 0
        and map[i][j - 1] - map[i][j] <= 1
        and (memoization[i][j - 1] is None or length < memoization[i][j - 1])
    ):
        memoization[i][j - 1] = length
        lengths.append(shortest_path(i, j - 1, map, memoization, end))

    if (
        i < len(map) - 1
        and map[i + 1][j] - map[i][j] <= 1
        and (memoization[i + 1][j] is None or length < memoization[i + 1][j])
    ):
        memoization[i + 1][j] = length
        lengths.append(shortest_path(i + 1, j, map, memoization, end))

    if (
        j < len(map[0]) - 1
        and map[i][j + 1] - map[i][j] <= 1
        and (memoization[i][j + 1] is None or length < memoization[i][j + 1])
    ):
        memoization[i][j + 1] = length
        lengths.append(shortest_path(i, j + 1, map, memoization, end))

    if len(lengths) == 0:
        return len(map) * len(map[0])
    return min(lengths)


def part_1(map, verbose):
    memoization = [[None for _ in range(len(map[0]))] for _ in range(len(map))]
    integer_map = [[26 - ord(i) + ord("a") for i in line] for line in map]
    for i, x in enumerate(map):
        if "S" in x:
            j = x.index("S")
            integer_map[i][j] = 27
    for i, x in enumerate(map):
        if "E" in x:
            j = x.index("E")
            integer_map[i][j] = 0
            memoization[i][j] = 0
            return shortest_path(i, j, integer_map, memoization, 27)


def part_2(map, verbose):
    memoization = [[None for _ in range(len(map[0]))] for _ in range(len(map))]
    integer_map = [[26 - ord(i) + ord("a") for i in line] for line in map]
    for i, x in enumerate(map):
        if "S" in x:
            j = x.index("S")
            integer_map[i][j] = 27
    for i, x in enumerate(map):
        if "E" in x:
            j = x.index("E")
            integer_map[i][j] = 0
            memoization[i][j] = 0
            return shortest_path(i, j, integer_map, memoization, 26)


def main(args):
    map = read_strings(args.data_file)
    print(part_1(map, args.verbose))
    print(part_2(map, args.verbose))
