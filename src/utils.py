import re


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


def read_pairs(file):
    output = []
    with open(file) as f:
        lines = f.read().splitlines()
    for line in lines:
        output.append([int(i) for pair in line.split(",") for i in pair.split("-")])
    return output


def read_crates(file):
    with open(file) as f:
        lines = f.read().splitlines()
    n_crates = len(lines[0]) // 4 + 1  # last crates has a length of 3
    crates = {f"{i + 1}": [] for i in range(n_crates)}
    commands = []
    first_part = True
    for line in lines:
        if line == "" or line[1] == "1":
            first_part = False
            continue
        if first_part:
            for i in range(n_crates):
                letter = line[4 * i + 1]
                if letter != " ":
                    crates[str(i + 1)].insert(0, letter)
        else:
            commands.append([int(i) for i in re.findall(r"\d+", line)])
    return crates, commands


def read_raw_txt(file):
    with open(file) as f:
        raw = f.read().strip()
    return raw


def read_filesystem(file):
    def get_dic_path(dic, path):
        return get_dic_path(dic[path[0]], path[1:]) if path else dic

    with open(file) as f:
        lines = f.read().splitlines()

    filesystem = {"/": {}}
    path = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[:4] == "$ ls":
            while i + 1 < len(lines) and lines[i + 1][0] != "$":
                i += 1
                line = lines[i]
                if line[:3] == "dir":
                    get_dic_path(filesystem, path)[line[4:]] = {}
                else:
                    size, filename = line.split()
                    get_dic_path(filesystem, path)[filename] = int(size)
        elif line[:7] == "$ cd ..":
            path.pop()
        elif line[:4] == "$ cd":
            get_dic_path(filesystem, path)[line[5:]] = get_dic_path(
                filesystem, path
            ).get(line[5:], {})
            path.append(line[5:])
        i += 1
    return filesystem
