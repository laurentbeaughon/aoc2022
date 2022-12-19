from tqdm import tqdm

from utils import read_robots_setups


def solver(setups, part, verbose):
    def solve(setup, inventory, robots, time):
        """
        setup: {
            "ore": ore,
            "clay": ore,
            "obsidian": ore, clay,
            "geode": ore, obsidian,
        }
        inventory: [ore, clay, obsidian, geode]
        robots: [ore, clay, obsidian, geode]
        """
        if (
            MEMOIZATION.get(
                f"{inventory[0]}, {inventory[1]}, {inventory[2]}, {inventory[3]}, {robots[0]}, {robots[1]}, {robots[2]}, {robots[3]}, {time}",
                -1,
            )
            >= 0
        ):
            return MEMOIZATION.get(
                f"{inventory[0]}, {inventory[1]}, {inventory[2]}, {inventory[3]}, {robots[0]}, {robots[1]}, {robots[2]}, {robots[3]}, {time}"
            )
        if time == 0:
            return inventory[3]
        if time == 1 and inventory[2] < setup["geode"][1]:
            return inventory[3] + robots[3]
        if time == 2 and inventory[2] + robots[2] < setup["geode"][1]:
            return inventory[3] + 2 * robots[3]

        # build geode
        if inventory[0] >= setup["geode"][0] and inventory[2] >= setup["geode"][1]:
            n_inventory = [
                inventory[0] + robots[0] - setup["geode"][0],
                inventory[1] + robots[1],
                inventory[2] + robots[2] - setup["geode"][1],
                inventory[3] + robots[3],
            ]
            n_robots = [robots[0], robots[1], robots[2], robots[3] + 1]
            max_geode = solve(setup, n_inventory, n_robots, time - 1)
            MEMOIZATION[
                f"{inventory[0]}, {inventory[1]}, {inventory[2]}, {inventory[3]}, {robots[0]}, {robots[1]}, {robots[2]}, {robots[3]}, {time}"
            ] = max_geode
            return max_geode

        # do nothing
        n_inventory = [
            inventory[0] + robots[0],
            inventory[1] + robots[1],
            inventory[2] + robots[2],
            inventory[3] + robots[3],
        ]
        n_robots = [robots[0], robots[1], robots[2], robots[3]]
        max_geode = max(n_inventory[3], solve(setup, n_inventory, n_robots, time - 1))

        # build ore robot
        if (
            inventory[0] >= setup["ore"]
            and robots[0]
            < max(setup["ore"], setup["clay"], setup["obsidian"][0], setup["geode"][0])
            and inventory[0]
            < max(setup["ore"], setup["clay"], setup["obsidian"][0], setup["geode"][0])
            + robots[0]
        ):
            n_inventory = [
                inventory[0] + robots[0] - setup["ore"],
                inventory[1] + robots[1],
                inventory[2] + robots[2],
                inventory[3] + robots[3],
            ]
            n_robots = [robots[0] + 1, robots[1], robots[2], robots[3]]
            max_geode = max(max_geode, solve(setup, n_inventory, n_robots, time - 1))

        # build clay robot
        if inventory[0] >= setup["clay"] and robots[1] < setup["obsidian"][1]:
            n_inventory = [
                inventory[0] + robots[0] - setup["clay"],
                inventory[1] + robots[1],
                inventory[2] + robots[2],
                inventory[3] + robots[3],
            ]
            n_robots = [robots[0], robots[1] + 1, robots[2], robots[3]]
            max_geode = max(max_geode, solve(setup, n_inventory, n_robots, time - 1))

        # build obsidian robot
        if (
            inventory[0] >= setup["obsidian"][0]
            and inventory[1] >= setup["obsidian"][1]
            and robots[2] < setup["geode"][1]
        ):
            n_inventory = [
                inventory[0] + robots[0] - setup["obsidian"][0],
                inventory[1] + robots[1] - setup["obsidian"][1],
                inventory[2] + robots[2],
                inventory[3] + robots[3],
            ]
            n_robots = [robots[0], robots[1], robots[2] + 1, robots[3]]
            max_geode = max(max_geode, solve(setup, n_inventory, n_robots, time - 1))

        MEMOIZATION[
            f"{inventory[0]}, {inventory[1]}, {inventory[2]}, {inventory[3]}, {robots[0]}, {robots[1]}, {robots[2]}, {robots[3]}, {time}"
        ] = max_geode
        return max_geode

    if part == 1:
        output = 0
        i = 1
        for setup in tqdm(setups):
            MEMOIZATION = {}
            s = solve(setup, (0, 0, 0, 0), (1, 0, 0, 0), 24)
            output += i * s
            i += 1
        # print(MEMOIZATION)
        return output

    if part == 2:
        output = 1
        for setup in tqdm(setups[:3]):
            MEMOIZATION = {}
            s = solve(setup, (0, 0, 0, 0), (1, 0, 0, 0), 32)
            output *= s
        # print(MEMOIZATION)
        return output


def main(args):
    setups = read_robots_setups(args.data_file)
    print(solver(setups, 1, args.verbose))
    print(solver(setups, 2, args.verbose))
