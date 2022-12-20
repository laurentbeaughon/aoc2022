from tqdm import tqdm
from utils import read_integers


def part_1(list, verbose):
    length = len(list)
    indexes = [i for i in range(length)]
    for i, x in tqdm(enumerate(list)):
        start = indexes[i]
        move = x % (length - 1)
        if start + move >= length:
            move = -length + 1 + move
        if move >= 0:
            for j, index in enumerate(indexes):
                if index > start and index <= (start + move):
                    indexes[j] = indexes[j] - 1
        elif move < 0:
            for j, index in enumerate(indexes):
                if index < start and index >= (start + move):
                    indexes[j] = indexes[j] + 1
        indexes[i] = (indexes[i] + move) % length
    index_0 = indexes[list.index(0)]
    return (
        list[indexes.index((index_0 + 1000) % length)]
        + list[indexes.index((index_0 + 2000) % length)]
        + list[indexes.index((index_0 + 3000) % length)]
    )


def part_2(list, verbose):
    length = len(list)
    indexes = [i for i in range(length)]
    for _ in range(10):
        for i, x in tqdm(enumerate(list)):
            start = indexes[i]
            move = (x * 811589153) % (length - 1)
            if start + move >= length:
                move = -length + 1 + move
            if move >= 0:
                for j, index in enumerate(indexes):
                    if index > start and index <= (start + move):
                        indexes[j] = indexes[j] - 1
            elif move < 0:
                for j, index in enumerate(indexes):
                    if index < start and index >= (start + move):
                        indexes[j] = indexes[j] + 1
            indexes[i] = (indexes[i] + move) % length
    index_0 = indexes[list.index(0)]
    return 811589153 * (
        list[indexes.index((index_0 + 1000) % length)]
        + list[indexes.index((index_0 + 2000) % length)]
        + list[indexes.index((index_0 + 3000) % length)]
    )


def main(args):
    list = read_integers(args.data_file)
    print(part_1(list, args.verbose))
    print(part_2(list, args.verbose))
