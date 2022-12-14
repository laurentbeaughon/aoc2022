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
        output.append(
            [int(i) for pair in line.split(",") for i in pair.split("-")],
        )
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
                filesystem,
                path,
            ).get(line[5:], {})
            path.append(line[5:])
        i += 1
    return filesystem


def read_integers_map(file):
    with open(file) as f:
        output = [[int(i) for i in line] for line in f.read().splitlines()]
    return output


def read_movements(file):
    with open(file) as f:
        output = [(a[0], int(a[1:])) for a in f.read().splitlines()]
    return output


def read_cpu_instructions(file):
    with open(file) as f:
        lines = f.read().splitlines()
        output = [0 if line == "noop" else int(line[5:]) for line in lines]
    return output


def read_monkey_notes(file):
    def read_monkey_note(lines):
        items = [int(x) for x in lines[1][18:].split(", ")]
        if lines[2][23] == "+":
            operation = "add"
        elif lines[2][23] == "*":
            operation = "multiply"
        if lines[2][23:] == "* old":
            operation = "square"
            operation_value = None
        else:
            operation_value = int(lines[2][25:])
        test = int(lines[3][21:])
        true = int(lines[4][28:])
        false = int(lines[5][29:])
        return {
            "items": items,
            "operation": operation,
            "operation_value": operation_value,
            "test": test,
            "true": true,
            "false": false,
        }

    monkeys_data = []
    with open(file) as f:
        lines = f.read().splitlines()
        for i in range(len(lines) // 7 + 1):
            monkeys_data.append(read_monkey_note(lines[7 * i : 7 * (i + 1)]))
    return monkeys_data


def read_strings(file):
    with open(file) as f:
        return f.read().splitlines()


def read_pair_lists_characters(file):
    with open(file) as f:
        data = f.read().strip()
        data = data.replace("[", "[,").replace("]", ",]").split("\n\n")
    output = []
    for lists in data:
        list1, list2 = lists.split("\n")
        output.append(
            [
                [int(x) if x.isdigit() else x for x in list1.split(",") if x],
                [int(x) if x.isdigit() else x for x in list2.split(",") if x],
            ],
        )
    return output


def read_rock_structures(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return [
        [
            (int(pos.split(",")[0]), int(pos.split(",")[1]))
            for pos in re.split(" -> ", line)
        ]
        for line in lines
    ]


def read_sensors(file):
    with open(file) as f:
        lines = f.read().splitlines()
    pos = [[int(d) for d in re.findall("-?\d+", line)] for line in lines]
    return [[(r[0], r[1]), (r[2], r[3])] for r in pos]


def read_valve(file):
    valves = {}

    with open(file) as f:
        lines = f.read().splitlines()
    for line in lines:
        flow_rate = re.findall("\d+", line)[0]
        paths = re.findall("[A-Z]+", line)[2:]
        valves[line[6:8]] = [int(flow_rate), paths]
    return valves


def read_xyz_pos(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return {tuple(int(x) for x in line.split(",")) for line in lines}


def read_robots_setups(file):
    with open(file) as f:
        lines = f.read().splitlines()
    numbers = [re.findall(r"\d+", line) for line in lines]
    return [
        {
            "ore": int(n[1]),
            "clay": int(n[2]),
            "obsidian": (int(n[3]), int(n[4])),
            "geode": (int(n[5]), int(n[6])),
        }
        for n in numbers
    ]


def read_integers(file):
    with open(file) as f:
        return [int(line) for line in f.read().splitlines()]


def read_monkey_operations(file):
    with open(file) as f:
        lines = f.read().splitlines()
    output = {}
    for line in lines:
        monkey = line[:4]
        if line[6:].isdigit():
            output[monkey] = ("val", int(line[6:]))
        elif line[11] == "+":
            output[monkey] = ("sum", [line[6:10], line[13:]])
        elif line[11] == "-":
            output[monkey] = ("min", [line[6:10], line[13:]])
        elif line[11] == "*":
            output[monkey] = ("mul", [line[6:10], line[13:]])
        elif line[11] == "/":
            output[monkey] = ("div", [line[6:10], line[13:]])
    return output


def read_map_and_path(file):
    with open(file) as f:
        lines = f.read().splitlines()
    map = [
        [
            -1
            for _ in range(max([len(line) for line in lines[:-2]]))
        ] 
        for _ in range(len(lines) - 2)
    ]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == ".":
                map[i][j] = 0
            elif char == "#":
                map[i][j] = 1
    commands = []
    direction = 0
    val = 0
    for char in lines[-1]:
        if char.isdigit():
            val = val*10 + int(char)
        else:
            commands.append((val, direction))
            val = 0
        if char == "R":
            direction = (direction + 1) % 4
        if char == "L":
            direction = (direction - 1) % 4
    if val != 0:
        commands.append((val, direction))
    return map, commands


def read_elves_pos(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return {(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "#"}


def read_wind_map(file):
    with open(file) as f:
        lines = f.read().splitlines()

    m = {
        "<":(0,-1),
        ">":(0,1),
        "v":(1,0),
        "^":(-1,0)
    }

    return [
        [i-1, j-1, m[lines[i][j]]]
        for i in range(1,len(lines)-1)
        for j in range(1,len(lines[0])-1)
        if lines[i][j] != "."
    ], (len(lines)-2, len(lines[0])-2)
