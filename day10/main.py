"""Day 10: Adapter Array"""

from collections import Counter, defaultdict


def diff_counts(jolts):
    diffs = Counter([b - a for a, b in zip(jolts, jolts[1:-1])])
    return diffs[1] * (diffs[3] + 1)


def count_paths(jolts: set):
    paths = defaultdict(int)
    paths[0] = 1

    for j in jolts[1:]:
        paths[j] = paths[j-1] + paths[j-2] + paths[j-3]

    return paths


with open('input.txt') as f:
    jolts = sorted([int(l) for l in f.readlines()])
    jolts = [0, *jolts, jolts[-1] + 3]

    print('part 1:', diff_counts(jolts))
    print('part 2:', count_paths(jolts)[max(jolts)])
