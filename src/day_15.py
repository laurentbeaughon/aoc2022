from tqdm import tqdm
from utils import read_sensors


def part_1(sensors, verbose):
    beacon_impossible = set()
    for sensor, beacon in sensors:
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if (zone_range := abs(sensor[1] - 2_000_000)) < dist:
            beacon_impossible.update(
                range(sensor[0] - (dist - zone_range), sensor[0] + (dist - zone_range))
            )
    return len(beacon_impossible)


def part_2(sensors, verbose):
    possible_beacons = set()
    for sensor, beacon in tqdm(sensors):
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for i in range(dist + 2):
            possible_beacons.add((sensor[0] + dist + 1 - i, sensor[1] + i))
            possible_beacons.add((sensor[0] + dist + 1 - i, sensor[1] - i))
            possible_beacons.add((sensor[0] - dist - 1 + i, sensor[1] + i))
            possible_beacons.add((sensor[0] - dist - 1 + i, sensor[1] - i))
    for possible_beacon in tqdm(possible_beacons):
        if (
            0 <= possible_beacon[0] <= 4_000_000
            and 0 <= possible_beacon[1] <= 4_000_000
        ):
            possible = True
            for sensor, beacon in sensors:
                dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
                if (
                    possible
                    and abs(sensor[1] - possible_beacon[1])
                    + abs(sensor[0] - possible_beacon[0])
                    <= dist
                ):
                    possible = False
            if possible:
                print(possible_beacon[0], possible_beacon[1])
                return 4_000_000 * possible_beacon[0] + possible_beacon[1]
    return possible_beacons


def main(args):
    sensors = read_sensors(args.data_file)
    print(part_1(sensors, args.verbose))
    print(part_2(sensors, args.verbose))
