from utils import read_cpu_instructions


def part_1(instructions, verbose):
    x = 1
    i = 1
    signal_strength = [0]
    for instruction in instructions:
        signal_strength.append(i * x)
        i += 1
        if instruction != 0:
            signal_strength.append(i * x)
            x += instruction
            i += 1
    score = (
        signal_strength[20]
        + signal_strength[60]
        + signal_strength[100]
        + signal_strength[140]
        + signal_strength[180]
        + signal_strength[220]
    )
    return score


def part_2(instructions, verbose):
    def show_pixels(pixels):
        print("".join(pixels[:40]))
        print("".join(pixels[40:80]))
        print("".join(pixels[80:120]))
        print("".join(pixels[120:160]))
        print("".join(pixels[160:200]))
        print("".join(pixels[200:240]))

    pixels = [" " for _ in range(240)]
    x = 1
    i = 0
    for instruction in instructions:
        if x <= i % 40 + 1 and x >= i % 40 - 1:
            pixels[i] = "█"
        i += 1
        if instruction != 0:
            if x <= i % 40 + 1 and x >= i % 40 - 1:
                pixels[i] = "█"
            x += instruction
            i += 1
    show_pixels(pixels)


def main(args):
    instructions = read_cpu_instructions(args.data_file)
    print(part_1(instructions, args.verbose))
    part_2(instructions, args.verbose)
