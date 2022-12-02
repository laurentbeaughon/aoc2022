from utils import read_rock_papper_scissors


def part_1(data, verbose):
    score = 0
    for round in data:
        score += round[1]
        if round[1] == round[0]:
            score += 3
        elif round[1] - round[0] == 1 or round[1] - round[0] == -2:
            score += 6
    return score


def part_2(data, verbose):
    score = 0
    for round in data:
        if round[1] == 1:
            score += (round[0] - 2) % 3 + 1
        elif round[1] == 2:
            score += 3 + round[0]
        elif round[1] == 3:
            score += 6 + round[0] % 3 + 1
    return score


def main(args):
    data = read_rock_papper_scissors(args.data_file)
    print(part_1(data, args.verbose))
    print(part_2(data, args.verbose))
