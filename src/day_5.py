from utils import read_crates


def part_1(data, commands, verbose):
    for command in commands:
        assert len(command) == 3
        if verbose:
            print(data)
            print(f"move {command[0]} from {command[1]} to {command[2]}")
        for i in range(command[0]):
            data[str(command[2])].append(data[str(command[1])].pop())
    return [data[str(i + 1)][-1] for i in range(len(data))]


def part_2(data, commands, verbose):
    for command in commands:
        assert len(command) == 3
        if verbose:
            print(data)
            print(f"move {command[0]} from {command[1]} to {command[2]}")
        data[str(command[2])] += data[str(command[1])][-command[0] :]
        data[str(command[1])] = data[str(command[1])][: -command[0]]
    return [data[str(i + 1)][-1] for i in range(len(data))]


def main(args):
    input_data, commands = read_crates(args.data_file)
    print(part_1(input_data, commands, args.verbose))
    input_data, commands = read_crates(args.data_file)
    print(part_2(input_data, commands, args.verbose))
