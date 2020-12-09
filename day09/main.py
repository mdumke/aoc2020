"""Day 9: Encoding Error"""

from itertools import combinations
from typing import Iterator, List

PREAMBLE = 25


def sliding_window(values, width) -> Iterator[List[int]]:
    return (values[i:i+width] for i in range(len(values)-width))


def has_pair_summing_to(target, values) -> bool:
    return any((sum(pair) == target for pair in combinations(values, 2)))


def find_batch_summing_to(target, batch_size, values) -> List[int]:
    return next((batch
                 for batch in sliding_window(values, batch_size)
                 if sum(batch) == target), None)


def find_first_invalid_number(xmas) -> int:
    return next(number
                for *preamble, number in sliding_window(xmas, PREAMBLE+1)
                if not has_pair_summing_to(number, preamble))


def find_encryption_weakness(xmas, invalid_number) -> int:
    for batch_size in range(2, len(xmas)):
        if (batch := find_batch_summing_to(invalid_number, batch_size, xmas)):
            return min(batch) + max(batch)


if __name__ == '__main__':
    with open('input.txt') as f:
        xmas = [int(n) for n in f.readlines()]

    first_invalid = find_first_invalid_number(xmas)
    print('part 1:', first_invalid)
    print('part 2:', find_encryption_weakness(xmas, first_invalid))
