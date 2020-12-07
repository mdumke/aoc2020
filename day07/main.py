"""Day 7: Handy Haversacks"""

import re


def contains_gold(bag, rules):
    return any([inner_bag == 'shiny gold' or contains_gold(inner_bag, rules)
                for inner_bag in rules[bag]])


def count_containing_bags(bag, rules):
    return sum([n + n * count_containing_bags(inner_bag, rules)
                for inner_bag, n in rules[bag].items()])


def load_puzzle_input():
    """returns dict with format {bag: {inner_bag: n}}"""
    def parse_line(line):
        (_, bag), *inner = re.findall(r'(\d+|no)? ?(\w+ \w+) bags?', line)
        return bag, {inner_bag: int(n) for n, inner_bag in inner if n}

    with open('input.txt') as f:
        return dict(map(parse_line, f.readlines()))


if __name__ == '__main__':
    rules = load_puzzle_input()
    print('part 1', sum([contains_gold(bag, rules) for bag in rules]))
    print('part 2:', count_containing_bags('shiny gold', rules))
