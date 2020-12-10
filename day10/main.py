"""Day 10: Adapter Array"""

from functools import lru_cache


def jolt_gaps(adapters):
    jolts = sorted(list(adapters))

    previous = 0
    ones, threes = 0, 0

    for jolt in jolts:
        diff = jolt - previous

        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1

        previous = jolt

    return ones * (threes + 1)


def count_paths(adapters):
    target = max(adapters) + 3

    @lru_cache(128)
    def count_paths_to_target(current):
        if current + 3 == target:
            return 1

        paths = 0

        for i in [1, 2, 3]:
            if current + i in adapters:
                paths += count_paths_to_target(current + i)

        return paths

    return count_paths_to_target(0)


with open('input.txt') as f:
    adapters = set([int(l) for l in f.readlines()])

    print('part 1:', jolt_gaps(adapters))
    print('part 2:', count_paths(adapters))
