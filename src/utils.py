def read_batch_integers(file):
    output = []
    with open(file) as f:
        lines = f.read().splitlines()
    elf = []
    for line in lines:
        if line != "":
            elf.append(int(line))
        else:
            output.append(elf)
            elf = []
    return output


def read_rock_papper_scissors(file):
    output = []
    score = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    with open(file) as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        output.append((score[line[0]], score[line[1]]))
    return output


def read_ruckstacks(file):
    output = []
    with open(file) as f:
        lines = f.read().splitlines()
    for line in lines:
        middle = len(line.strip()) // 2
        output.append((line[:middle], line[middle:]))
    return output
