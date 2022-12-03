from utils import read_ruckstacks


def priority(letter, verbose):
    if verbose:
        print(letter)
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def part_1(data, verbose):
    priorities = 0
    for ruckstack in data:
        common_item = set(ruckstack[0]).intersection(set(ruckstack[1]))
        assert len(common_item) == 1
        priorities += priority(common_item.pop(), verbose)
    return priorities


def part_2(data, verbose):
    priorities = 0
    for i in range(0, len(data), 3):
        items1 = set(data[i][0]).union(set(data[i][1]))
        items2 = set(data[i + 1][0]).union(set(data[i + 1][1]))
        items3 = set(data[i + 2][0]).union(set(data[i + 2][1]))
        common_item = items1.intersection(items2, items3)
        assert len(common_item) == 1
        priorities += priority(common_item.pop(), verbose)
    return priorities


def main(args):
    data = read_ruckstacks(args.data_file)
    print(part_1(data, args.verbose))
    print(part_2(data, args.verbose))
