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
            elf=[]
    return output
