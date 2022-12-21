from tqdm import tqdm
from utils import read_monkey_operations

import matplotlib.pyplot as plt


def part_1(monkeys, verbose):
    def compute(monkey):
        state = monkeys[monkey]
        if state[0] == "val":
            return state[1]
        elif state[0] == "sum":
            return compute(state[1][0]) + compute(state[1][1])
        elif state[0] == "min":
            return compute(state[1][0]) - compute(state[1][1])
        elif state[0] == "mul":
            return compute(state[1][0]) * compute(state[1][1])
        elif state[0] == "div":
            return compute(state[1][0]) / compute(state[1][1])

    return compute("root")


def part_2(monkeys, verbose):
    def compute(monkey):
        state = monkeys[monkey]
        if state[0] == "val":
            return state[1]
        elif state[0] == "sum":
            return compute(state[1][0]) + compute(state[1][1])
        elif state[0] == "min":
            return compute(state[1][0]) - compute(state[1][1])
        elif state[0] == "mul":
            return compute(state[1][0]) * compute(state[1][1])
        elif state[0] == "div":
            return compute(state[1][0]) / compute(state[1][1])

    x = []
    y = []
    for i in tqdm(
        range(3093175982500, 3093175982600)
    ):  # manual dichotomie (beautiful code here)
        monkeys["humn"] = ("val", 10**0 * i)
        a = compute(monkeys["root"][1][0])
        b = compute(monkeys["root"][1][1])
        x.append(a)
        y.append(b)
        if a == b:
            return i
    plt.plot([i for i in range(len(x))], x)
    plt.plot([i for i in range(len(y))], y)
    plt.show()
    return "not found"


def main(args):
    monkeys = read_monkey_operations(args.data_file)
    print(part_1(monkeys, args.verbose))
    print(part_2(monkeys, args.verbose))
