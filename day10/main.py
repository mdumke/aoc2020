"""Day 10: Adapter Array"""

from functools import lru_cache
from collections import Counter


def diff_counts(jolts):
    diffs = Counter([b - a for a, b in zip([0, *jolts], jolts)])
    return diffs[1] * (diffs[3] + 1)


def count_paths(adapters: set):
    final = max(adapters)

    @lru_cache
    def count_from(i):
        if i == final:
            return 1
        return sum([count_from(j) for j in (i+1, i+2, i+3) if j in adapters])

    return count_from(0)


with open('input.txt') as f:
    adapters = set([int(l) for l in f.readlines()])

    print('part 1:', diff_counts(sorted(adapters)))
    print('part 2:', count_paths(adapters))
