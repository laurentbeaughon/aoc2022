from utils import read_raw_txt


def detect(string, size):
    for i in range(len(string) - size):
        if len(set(string[i : i + size])) == size:
            return i + size
    return 0


def part_1(string, verbose):
    return detect(string, 4)


def part_2(string, verbose):
    return detect(string, 14)


def main(args):
    raw = read_raw_txt(args.data_file)
    print(part_1(raw, args.verbose))
    print(part_2(raw, args.verbose))
