from utils import read_wind_map


def part_1(wind_map, dimensions, verbose):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0))
    
    def run_timestamp():
        for x in wind_map:
            i, j, wind_direction = x
            ni = (i + wind_direction[0]) % dimensions[0]
            nj = (j + wind_direction[1]) % dimensions[1]
            x[0], x[1] = ni, nj


    start = (-1, 0)
    arrival = (dimensions[0], dimensions[1] - 1)
    path = []
    path.append((start, 0))
    memoization = set()
    maxdist = -1
    pos, timestamp = path.pop(0)
    while pos != arrival:
        if timestamp > maxdist:
            maxdist = timestamp
            run_timestamp()
            walls = {(i, j) for i, j, _ in wind_map}

        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in walls and 0 <= new_pos[0] < dimensions[0] and 0 <= new_pos[1] < dimensions[1] or new_pos in [start, arrival]:
                if (new_pos, timestamp) not in memoization:
                    memoization.add((new_pos, timestamp))
                    path.append((new_pos, timestamp + 1))
        pos, timestamp = path.pop(0)

    print(f"first arrival {timestamp}")

    start = (dimensions[0], dimensions[1] - 1)
    arrival = (-1, 0)
    path = []
    path.append((start, timestamp))
    pos, timestamp = path.pop(0)
    while pos != arrival:
        if timestamp > maxdist:
            maxdist = timestamp
            run_timestamp()
            walls = {(i, j) for i, j, _ in wind_map}

        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in walls and 0 <= new_pos[0] < dimensions[0] and 0 <= new_pos[1] < dimensions[1] or new_pos in [start, arrival]:
                if (new_pos, timestamp) not in memoization:
                    memoization.add((new_pos, timestamp))
                    path.append((new_pos, timestamp + 1))
        pos, timestamp = path.pop(0)

    print(f"returning back {timestamp}")
    
    start = (-1, 0)
    arrival = (dimensions[0], dimensions[1] - 1)
    path = []
    path.append((start, timestamp))
    pos, timestamp = path.pop(0)
    while pos != arrival:
        if timestamp > maxdist:
            maxdist = timestamp
            run_timestamp()
            walls = {(i, j) for i, j, _ in wind_map}

        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in walls and 0 <= new_pos[0] < dimensions[0] and 0 <= new_pos[1] < dimensions[1] or new_pos in [start, arrival]:
                if (new_pos, timestamp) not in memoization:
                    memoization.add((new_pos, timestamp))
                    path.append((new_pos, timestamp + 1))
        pos, timestamp = path.pop(0)

    print(f"second arrival {timestamp}")

def main(args):
    wind, dimensions = read_wind_map(args.data_file)
    part_1(wind, dimensions, args.verbose)
