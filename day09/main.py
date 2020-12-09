"""Day 9: Encoding Error"""

from itertools import combinations


def sum_to(target, values):
    for a, b in combinations(values, 2):
        if a + b == target:
            return True


def find_first_invalid(xmas):
    for i in range(25, len(xmas)):
        if not sum_to(xmas[i], xmas[i-25:i]):
            return xmas[i]


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
