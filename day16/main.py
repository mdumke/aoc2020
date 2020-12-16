import re

def is_valid_number(n, rules):
    for rule in rules:
        for lo, hi in rule:
            if lo <= n <= hi:
                return True

def parse_rule(line):
    return [(int(a), int(b)) for a, b in re.findall(r'(\d+)-(\d+)', line)]

def parse_ticket(line):
    return [int(n) for n in line.split(',')]


def load_puzzle_input():
    with open('input.txt') as f:
        rules, ticket, nearby = f.read().split('\n\n')

        return (
            [parse_rule(r) for r in rules.split('\n')],
            parse_ticket(ticket.split('\n')[1]),
            [parse_ticket(t) for t in nearby.strip().split('\n')[1:]])


if __name__ == '__main__':
    rules, ticket, nearby = load_puzzle_input()

    print('part 1:', sum([n for ticket in nearby for n in ticket if not is_valid_number(n, rules)]))
