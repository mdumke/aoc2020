"""Day 10: Adapter Array"""

from collections import Counter, defaultdict


def diff_counts(jolts):
    diffs = Counter([a - b for a, b in zip(jolts[1:], jolts)])
    return diffs[1] * diffs[3]


def count_paths(jolts):
    paths = defaultdict(int)
    paths[0] = 1

    for j in jolts[1:]:
        paths[j] = paths[j-1] + paths[j-2] + paths[j-3]

    return paths[jolts[-1]]


if __name__ == '__main__':
    with open('input.txt') as f:
        jolts = sorted([int(l) for l in f.readlines()])
        jolts = [0, *jolts, jolts[-1] + 3]

    print('part 1:', diff_counts(jolts))
    print('part 2:', count_paths(jolts))
