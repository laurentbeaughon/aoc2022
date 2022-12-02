def read_batch_integers(file):
    output = []
    with open(file) as f:
        lines = f.readlines()
    elf = []
    for line in lines:
        line = line.strip()
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
        lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        output.append((score[line[0]], score[line[1]]))
    return output
