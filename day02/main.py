#!/usr/bin/env python

"""Day 2: Password Philosophy"""

import re
from collections import namedtuple
from operator import countOf, xor


def count_valid_passwords(records, criterion):
    return sum(map(criterion, records))


def is_valid_by_old_policy(rec):
    count = countOf(rec.password, rec.char)
    return count >= rec.int1 and count <= rec.int2


def is_valid_by_new_policy(rec):
    match1 = rec.password[rec.int1-1] == rec.char
    match2 = rec.password[rec.int2-1] == rec.char
    return xor(match1, match2)


def load_puzzle_input():
    Record = namedtuple('Record', 'int1 int2 char password')
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

    def parse_line(l):
        int1, int2, char, pw = re.match(pattern, l).groups()
        return Record(int(int1), int(int2), char, pw)

    with open('input.txt') as f:
        return [parse_line(l) for l in f.readlines()]


if __name__ == '__main__':
    records = load_puzzle_input()
    print('part1:', count_valid_passwords(records, is_valid_by_old_policy))
    print('part2:', count_valid_passwords(records, is_valid_by_new_policy))
