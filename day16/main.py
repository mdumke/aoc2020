"""Day 16: Ticket Translation"""

import re
import math
import numpy as np
from more_itertools import flatten, sliced
from types import SimpleNamespace

OPEN, VALUE, CLOSE = '0-open', '1-value', '2-close'


def is_covered(value, ranges) -> bool:
    """returns True if the value falls into one of the ranges"""
    return any(a <= value <= b for a, b in ranges)


def get_invalid_values(values, ranges) -> [int]:
    """returns values that do not fall into any given range"""
    return [v for v in values if not is_covered(v, ranges)]


def filter_valid_tickets(tickets, ranges) -> np.ndarray:
    """returns only tickets with valid numbers"""
    return tickets[[i for i, t in enumerate(tickets) if all_covered(t, ranges)]]


def get_matching_rules(values, rules) -> [str]:
    """returns the names of all rules that cover the given values"""
    return [name for name, ranges in zip(rules.names, rules.ranges) if all_covered(values, ranges)]


def combine_ranges(ranges) -> [(int, int)]:
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

    return list(sliced(result, 2))


def all_covered(values, ranges) -> bool:
    """returns True if all values fall inside one of the ranges"""
    # create a sorted list like [(2, OPEN), (5, VALUE), (5, CLOSE)]
    # OPEN/CLOSE refer to the endpoints of a range
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


def get_departure_info(rules, my_ticket, tickets) -> [int]:
    """returns ticket-values in departure-fields"""
    valid_tickets = filter_valid_tickets(tickets, combine_ranges(rules.ranges))

    # [(0, ['class', 'seat']), ...]
    possible_fields = [(i, get_matching_rules(field, rules))
                       for i, field in enumerate(valid_tickets.T)]

    # {'class': 3}
    fields = {}
    for n, candidates in sorted(possible_fields, key=lambda f: len(f[1])):
        for field in candidates:
            if not fields.get(field):
                fields[field] = n

    # look up values from the ticket's departure fields
    return [my_ticket[i] for name, i in fields.items() if 'departure' in name]


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

    print('part 1:', sum(get_invalid_values(
        tickets.ravel(), combine_ranges(rules.ranges))))
    print('part 2:', math.prod(get_departure_info(rules, my_ticket, tickets)))
