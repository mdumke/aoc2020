"""Day 16: Ticket Translation"""


import re
import numpy as np
from more_itertools import flatten, sliced
from types import SimpleNamespace

OPEN, VALUE, CLOSE = '0-open', '1-value', '2-close'


def is_covered(value, ranges):
    return any(a <= value <= b for a, b in ranges)


def sum_invalid_values(values, ranges):
    return sum(v for v in values if not is_covered(v, ranges))


def combine_ranges(ranges):
    """Combines overlapping and adjacent ranges

    example:
    [(1, 2), (3, 4), (6, 7)] to [(1, 4), (6, 7)]
    """
    result = []

    for a, b in sorted(flatten(ranges)):
        if result and a <= result[-1] + 1:
            result[-1] = b
        else:
            result.extend((a, b))

    return [tuple(pair) for pair in sliced(result, 2)]


def is_valid_ticket(ticket, ranges):
    return all(is_covered(value, ranges) for value in ticket)


def filter_valid_tickets(tickets, ranges):
    return tickets[[i for i, t in enumerate(tickets) if is_valid_ticket(t, ranges)]]


def all_covered(values, ranges):
    """returns True if all values fall inside one of the ranges"""
    # create a sorted list like [(2, OPEN), (5, VALUE), (5, CLOSE)]
    numbers = sorted([
        *list(flatten([[(a, OPEN), (b, CLOSE)] for a, b in ranges])),
        *[(v, VALUE) for v in values]])

    # return False if a VALUE arrives while state is CLOSE
    prev_state = CLOSE
    for _, state in numbers:
        if state == VALUE and prev_state == CLOSE:
            return False

        prev_state = state

    return True


def get_matching_rules(values, rule_ranges, rule_names):
    """returns the names of all rules that match the given values"""
    return [name for name, ranges in zip(rule_names, rule_ranges) if all_covered(values, ranges)]


def part2(rule_names, rule_ranges, my_ticket, tickets):
    valid_tickets = filter_valid_tickets(tickets, combine_ranges(rule_ranges))
    possible_fields = []

    for i, field in enumerate(valid_tickets.T):
        matches = get_matching_rules(field, rule_ranges, rule_names)
        possible_fields.append((i, matches))

    fields = {}

    for n, candidates in sorted(possible_fields, key=lambda f: len(f[1])):
        for field in candidates:
            if not fields.get(field):
                fields[field] = n

    total = 1

    for name, position in fields.items():
        if 'departure' in name:
            total *= my_ticket[position]

    return total


def load_puzzle_input():
    """returns input-tuple with rules, my_ticket, tickets

    returns
    rules: SimpleNamespace(names: [str], ranges: [(int, int)])
    my_ticket: numpy.ndarray
    tickets: 2d numpy.ndarray
    """
    range_pattern = re.compile(r'(\d+)-(\d+)')

    def parse_ranges(line):
        ranges = line.split(':')[1]
        return [(int(a), int(b)) for a, b in re.findall(range_pattern, ranges)]

    def parse_rules(lines):
        names = [line.split(':')[0] for line in lines.split('\n')]
        ranges = [parse_ranges(line) for line in lines.split('\n')]
        return SimpleNamespace(names=names, ranges=ranges)

    def parse_tickets(lines):
        return np.array([[int(n) for n in line.strip().split(',')]
                         for line in lines.strip().split('\n')[1:]])

    with open('input.txt') as f:
        section1, section2, section3 = f.read().split('\n\n')

    return (
        parse_rules(section1),
        parse_tickets(section2)[0],
        parse_tickets(section3))


if __name__ == '__main__':
    rules, my_ticket, tickets = load_puzzle_input()

    print('part 1:', sum_invalid_values(
        tickets.ravel(), combine_ranges(rules.ranges)))
    print('part 2:', part2(rules.names, rules.ranges, my_ticket, tickets))
