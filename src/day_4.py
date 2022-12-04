from utils import read_pairs


def part_1(data, verbose):
    cpt = 0
    for pairs in data:
        if (
            pairs[0] >= pairs[2]
            and pairs[1] <= pairs[3]
            or pairs[2] >= pairs[0]
            and pairs[3] <= pairs[1]
        ):
            cpt += 1
    return cpt


def part_2(data, verbose):
    cpt = 0
    for pairs in data:
        if (
            pairs[2] <= pairs[1]
            and pairs[3] >= pairs[0]
            or pairs[2] >= pairs[1]
            and pairs[3] <= pairs[0]
        ):
            cpt += 1
    return cpt


def main(args):
    data = read_pairs(args.data_file)
    print(part_1(data, args.verbose))
    print(part_2(data, args.verbose))
