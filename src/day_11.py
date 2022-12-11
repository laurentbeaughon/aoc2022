from utils import read_monkey_notes


def part_1(monkeys_data, verbose):
    def run_round(monkeys_data, activity):
        for i, monkey in enumerate(monkeys_data):
            for worry_level in monkey["items"]:
                if monkey["operation"] == "add":
                    worry_level += monkey["operation_value"]
                if monkey["operation"] == "multiply":
                    worry_level *= monkey["operation_value"]
                if monkey["operation"] == "square":
                    worry_level *= worry_level
                worry_level = worry_level // 3
                if worry_level % monkey["test"] == 0:
                    monkeys_data[monkey["true"]]["items"].append(worry_level)
                else:
                    monkeys_data[monkey["false"]]["items"].append(worry_level)

                activity[i] += 1
                monkey["items"] = []
        return monkeys_data, activity

    activity = [0 for _ in range(len(monkeys_data))]
    for _ in range(20):
        monkeys_data, activity = run_round(monkeys_data, activity)
        if verbose:
            print([x["items"] for x in monkeys_data])
    activity.sort()
    return activity[-1] * activity[-2]


def part_2(monkeys_data, verbose):
    def run_round(monkeys_data, activity, division):
        for i, monkey in enumerate(monkeys_data):
            for worry_level in monkey["items"]:
                if monkey["operation"] == "add":
                    worry_level += monkey["operation_value"]
                if monkey["operation"] == "multiply":
                    worry_level *= monkey["operation_value"]
                if monkey["operation"] == "square":
                    worry_level *= worry_level
                worry_level %= division
                if worry_level % monkey["test"] == 0:
                    monkeys_data[monkey["true"]]["items"].append(worry_level)
                else:
                    monkeys_data[monkey["false"]]["items"].append(worry_level)

                activity[i] += 1
                monkey["items"] = []
        return monkeys_data, activity

    activity = [0 for _ in range(len(monkeys_data))]
    division = 1
    for monkey in monkeys_data:
        division *= monkey["test"]
    for _ in range(10000):
        monkeys_data, activity = run_round(monkeys_data, activity, division)
        if verbose:
            print([x["items"] for x in monkeys_data])
    activity.sort()
    return activity[-1] * activity[-2]


def main(args):
    monkeys_data = read_monkey_notes(args.data_file)
    print(monkeys_data)
    print(part_1(monkeys_data, args.verbose))
    monkeys_data = read_monkey_notes(args.data_file)
    print(part_2(monkeys_data, args.verbose))
