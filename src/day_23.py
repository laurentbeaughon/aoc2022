from tqdm import tqdm
from utils import read_elves_pos


def part_1(elves, verbose):
    directions = [
        [(-1, 1), (-1, 0), (-1, -1)],  # North
        [(1, 1), (1, 0), (1, -1)],  # South
        [(1, -1), (0, -1), (-1, -1)],  # West
        [(1, 1), (0, 1), (-1, 1)],  # Est
    ]
    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for _ in range(10):
        next_pos = {}
        for elf in elves:
            if all(
                (elf[0] + neighbor[0], elf[1] + neighbor[1]) not in elves
                for neighbor in neighbors
            ):
                next_pos[elf] = next_pos.get(elf, []) + [elf]
            else:
                for direction in directions:
                    if all(
                        (elf[0] + pos[0], elf[1] + pos[1]) not in elves
                        for pos in direction
                    ):
                        candidate = (elf[0] + direction[1][0], elf[1] + direction[1][1])
                        next_pos[candidate] = next_pos.get(candidate, []) + [elf]
                        break
                else:
                    next_pos[elf] = next_pos.get(elf, []) + [elf]
        elves = set()
        for new, old in next_pos.items():
            if len(old) == 1:
                elves.add(new)
            else:
                elves.update(old)
        directions = directions[1:] + [directions[0]]

    width = max(elves, key=lambda x:x[1])[1] - min(elves, key=lambda x:x[1])[1] + 1
    height = max(elves, key=lambda x:x[0])[0] - min(elves, key=lambda x:x[0])[0] + 1
    print(width)
    print(height)
    return width * height - len(elves)

    
def part_2(elves, verbose):
    directions = [
        [(-1, 1), (-1, 0), (-1, -1)],  # North
        [(1, 1), (1, 0), (1, -1)],  # South
        [(1, -1), (0, -1), (-1, -1)],  # West
        [(1, 1), (0, 1), (-1, 1)],  # Est
    ]
    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    moving = True
    i = 0
    while moving:
        moving = False
        next_pos = {}
        for elf in elves:
            if all(
                (elf[0] + neighbor[0], elf[1] + neighbor[1]) not in elves
                for neighbor in neighbors
            ):
                next_pos[elf] = next_pos.get(elf, []) + [elf]
            else:
                for direction in directions:
                    if all(
                        (elf[0] + pos[0], elf[1] + pos[1]) not in elves
                        for pos in direction
                    ):
                        moving = True
                        candidate = (elf[0] + direction[1][0], elf[1] + direction[1][1])
                        next_pos[candidate] = next_pos.get(candidate, []) + [elf]
                        break
                else:
                    next_pos[elf] = next_pos.get(elf, []) + [elf]
        elves = set()
        for new, old in next_pos.items():
            if len(old) == 1:
                elves.add(new)
            else:
                elves.update(old)
        directions = directions[1:] + [directions[0]]
        i += 1
    return i


def main(args):
    elves = read_elves_pos(args.data_file)
    print(part_1(elves, args.verbose))
    print(part_2(elves, args.verbose))
