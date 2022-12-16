from time import time
from tqdm import tqdm

from utils import read_valve


def preprocess_valves(valves):
    def length(v1, v2, visited=set()):
        if v1 == v2:
            return 0
        shortest_length = len(valves)
        for v3 in valves[v1][1]:
            if v3 not in visited:
                new_visited = visited.copy()
                new_visited.add(v1)
                shortest_length = min(shortest_length, 1 + length(v3, v2, new_visited))
        return shortest_length

    relevant_valves = [valve for valve in valves if valves[valve][0] > 0] + ["AA"]
    simplify_valves = {}
    for valve1 in tqdm(relevant_valves):
        paths = {}
        for valve2 in relevant_valves:
            if valve1 != valve2:
                paths[valve2] = length(valve1, valve2)
        simplify_valves[valve1] = (valves[valve1][0], paths)
    return simplify_valves


def part_1(valves, verbose):
    MAX_PRESSURE_VALVES = {}

    def max_pressure(position, open_valves, time_left):
        if time_left <= 0:
            return 0
        if (
            MAX_PRESSURE_VALVES.get(position + "".join(open_valves) + str(time_left), 0)
            != 0
        ):
            return MAX_PRESSURE_VALVES[position + "".join(open_valves) + str(time_left)]
        _max_pressure = 0
        if position not in open_valves:
            pressure = (time_left - 1) * valves[position][0]
            new_open_valves = open_valves.copy()
            new_open_valves.append(position)
            new_open_valves.sort()
            if position == "AA":
                # Hack for AA null flow
                new_open_valves = open_valves.copy()
                time_left += 1
            for next_valve, length in valves[position][1].items():
                if next_valve not in open_valves:
                    _max_pressure = max(
                        _max_pressure,
                        pressure
                        + max_pressure(
                            next_valve, new_open_valves, time_left - 1 - length
                        ),
                    )
        MAX_PRESSURE_VALVES[
            position + "".join(open_valves) + str(time_left)
        ] = _max_pressure
        return _max_pressure

    return max_pressure("AA", [], 30)


def part_2(valves, verbose):
    MAX_PRESSURE_VALVES = {}

    def optimize(nextpos, nextmov):
        pressures = [valves[valve][0] for valve in nextpos]
        max_mov = nextmov[pressures.index(max(pressures))]
        min_pressure = pressures[nextmov.index(min(nextmov))]
        new_valves, new_distances = [], []
        for i in range(len(nextpos)):
            if nextmov[i] <= max_mov and pressures[i] >= min_pressure:
                # let's remove valves that are further with less pressure than another one
                new_valves.append(nextpos[i])
                new_distances.append(nextmov[i])
        return new_valves, new_distances

    def max_pressure(positions, movement, open_valves, time_left):
        if time_left <= 0:
            return 0
        if (
            MAX_PRESSURE_VALVES.get(
                positions[0] + positions[1] + "".join(open_valves) + str(time_left), 0
            )
            != 0
        ):
            return MAX_PRESSURE_VALVES[
                positions[0] + positions[1] + "".join(open_valves) + str(time_left)
            ]
        _max_pressure = 0

        if movement[0] > 0 and movement[1] > 0:
            return max_pressure(
                positions,
                (movement[0] - 1, movement[1] - 1),
                open_valves,
                time_left - 1,
            )

        pressure = 0
        new_open_valves = open_valves.copy()
        nextpos0 = []
        nextpos1 = []
        nextmovement0 = []
        nextmovement1 = []
        if movement[0] == 0:
            # we arrived at valve to open
            if positions[0] not in new_open_valves:
                # opening valve
                pressure += (time_left - 1) * valves[positions[0]][0]
                new_open_valves.append(positions[0])
                nextpos0 = [positions[0]]
                nextmovement0 = [1]  # to simulate 1 timestamp opening
            else:
                # Let's find next targets
                for valve, dist in valves[positions[0]][1].items():
                    if valve not in new_open_valves:
                        nextpos0.append(valve)
                        nextmovement0.append(dist)
            if len(nextpos0) == 0:
                # there are no more valve to open, let's start a long journey
                nextpos0.append("AA")
                nextmovement0.append(30)
            else:
                # remove targets that can't be optimal
                nextpos0, nextmovement0 = optimize(nextpos0, nextmovement0)
        else:
            nextmovement0 = [movement[0]]
            nextpos0 = [positions[0]]

        if movement[1] == 0:
            # same as above for elephant
            if positions[1] not in new_open_valves:
                pressure += (time_left - 1) * valves[positions[1]][0]
                new_open_valves.append(positions[1])
                nextpos1 = [positions[1]]
                nextmovement1 = [1]
            else:
                for valve, dist in valves[positions[1]][1].items():
                    if valve not in new_open_valves:
                        nextpos1.append(valve)
                        nextmovement1.append(dist)
            if len(nextpos1) == 0:
                nextpos1.append("AA")
                nextmovement1.append(30)
            else:
                nextpos1, nextmovement1 = optimize(nextpos1, nextmovement1)

        else:
            nextmovement1 = [movement[1]]
            nextpos1 = [positions[1]]

        for nm0, np0 in zip(nextmovement0, nextpos0):
            for nm1, np1 in zip(nextmovement1, nextpos1):
                _max_pressure = max(
                    _max_pressure,
                    pressure
                    + max_pressure(
                        (np0, np1), (nm0 - 1, nm1 - 1), new_open_valves, time_left - 1
                    ),
                )

        MAX_PRESSURE_VALVES[
            positions[0] + positions[1] + "".join(open_valves) + str(time_left)
        ] = _max_pressure
        return _max_pressure

    val = max_pressure(("AA", "AA"), (0, 0), ["AA"], 26)
    return val


def main(args):
    valves = read_valve(args.data_file)
    valves = preprocess_valves(valves)
    if args.verbose:
        print(valves)
    a = time()
    print(part_1(valves, args.verbose))
    b = time()
    print(f"part 1 duration: {b-a}s")
    print(part_2(valves, args.verbose))
    c = time()
    print(f"part 1 duration: {c-b}s")
