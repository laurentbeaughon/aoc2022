from utils import read_filesystem


SIZES = {}


def compute_size(filesystem, path):
    size = 0
    if SIZES.get(path, None):
        return SIZES[path]
    for name, part in filesystem.items():
        if type(part) is dict:
            size += compute_size(part, f"{path}/{name}")
        else:
            size += part
    SIZES[path] = size
    return size


def part_1(filesystem, verbose):
    compute_size(filesystem["/"], "")
    sum = 0
    for size in SIZES.values():
        if size <= 100_000:
            sum += size
    return sum


def part_2(filesystem, verbose):
    compute_size(filesystem["/"], "")
    size_to_delete = 30_000_000 - (70_000_000 - SIZES[""])
    to_delete = 70_000_000
    for size in SIZES.values():
        if size >= size_to_delete and size < to_delete:
            to_delete = size
    return to_delete


def main(args):
    filesystem = read_filesystem(args.data_file)
    print(part_1(filesystem, args.verbose))
    print(part_2(filesystem, args.verbose))
