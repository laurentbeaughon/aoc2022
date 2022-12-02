from utils import read_batch_integers


def part_1(data, verbose):
    max = 0
    for calories in data:
        if sum(calories) > max:
            max = sum(calories)
    return max


def part_2(data, verbose):
    calories = [sum(calorie) for calorie in data]
    calories.sort(reverse=True)
    return calories[0] + calories[1] + calories[2]


def main(args):
    data = read_batch_integers(args.data_file)
    print(part_1(data, args.verbose))
    print(part_2(data, args.verbose))
