"""Day 9: Encoding Error"""

from itertools import combinations

PREAMBLE = 25


def has_pair_summing_to(target, values):
    return any((sum(pair) == target for pair in combinations(values, 2)))


def sliding_window(values, width):
    return (values[i:i+width] for i in range(len(values)-width))


def find_first_invalid(xmas):
    return next(n for *preamble, n in sliding_window(xmas, PREAMBLE+1)
                if not has_pair_summing_to(n, preamble))


def find_encryption_weakness(xmas, target):
    for i in range(len(xmas)):
        cursor = i
        batch = []

        while sum(batch) < target:
            batch.append(xmas[cursor])
            cursor += 1

        if sum(batch) == target:
            return min(batch) + max(batch)


if __name__ == '__main__':
    with open('input.txt') as f:
        xmas = [int(n) for n in f.readlines()]

    first_invalid = find_first_invalid(xmas)
    print('part 1:', first_invalid)
    print('part 2:', find_encryption_weakness(xmas, first_invalid))
