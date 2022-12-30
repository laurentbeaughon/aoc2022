from utils import read_strings


def part_1(numbers, verbose):
    def SNAFU_to_int(number):
        char_to_dig = {
            "=": -2,
            "-": -1,
            "0": 0,
            "1": 1,
            "2": 2,
        }
        out = 0
        for x in number:
            out = out * 5 + char_to_dig[x]
        return out

    def int_to_SNAFU(number):
        dig_to_char = {
            -2: "=",
            -1: "-",
            0: "0",
            1: "1",
            2: "2",
        }
        out = []
        while number > 0:
            out.append(number % 5)
            number = number // 5
        out.append(0)
        for i in range(len(out)):
            if out[i] >= 3:
                out[i] = out[i] - 5
                out[i+1] += 1
        if out[-1] == 0:
            out.pop()
        return "".join([dig_to_char[dig] for dig in out[::-1]])


    sum = 0
    for number in numbers:
        sum += SNAFU_to_int(number)
    return int_to_SNAFU(sum)

def main(args):
    numbers = read_strings(args.data_file)
    print(part_1(numbers, args.verbose))
