from tqdm import tqdm

from utils import read_xyz_pos


neighbours = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def neighbours(x, y, z):
    neighbours = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return {
        (x + neighbour[0], y + neighbour[1], z + neighbour[2])
        for neighbour in neighbours
    }


def part_1(coordinates, verbose):
    output = 0
    for x, y, z in coordinates:
        for neighbour in neighbours(x, y, z):
            if neighbour not in coordinates:
                output += 1
    return output


def part_2(coordinates, verbose):
    def faces_lava(x, y, z):
        return any(cube in coordinates for cube in neighbours(x, y, z))

    def has_neighbor_facing_lava(x, y, z):
        return any(faces_lava(_x, _y, _z) for (_x, _y, _z) in neighbours(x, y, z))

    def flood(visited, limit):
        if not limit:
            return visited

        nlimit = {
            (_x, _y, _z)
            for (x, y, z) in limit
            for (_x, _y, _z) in neighbours(x, y, z) - visited - coordinates
            if faces_lava(_x, _y, _z) or has_neighbor_facing_lava(_x, _y, _z)
        }

        return flood(visited.union(limit), nlimit)

    def find_exterior():
        (minx, miny, minz) = min(coordinates)
        return flood(set(), {(minx - 1, miny, minz)})

    output = 0
    for x, y, z in find_exterior():
        for neighbour in neighbours(x, y, z):
            if neighbour in coordinates:
                output += 1
    return output


def main(args):
    coordinates = read_xyz_pos(args.data_file)
    print(part_1(coordinates, args.verbose))
    print(part_2(coordinates, args.verbose))
