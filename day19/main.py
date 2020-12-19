"""Day 19: Monster Messages"""


def is_valid(message, rules):
    fringe = [(message, rules[0])]

    while fringe:
        msg, rule = fringe.pop()

        if not msg and not rule:
            return True

        if not msg or not rule:
            continue

        if isinstance(rule[0], str) and rule[0] == msg[0]:
            fringe.append((msg[1:], rule[1:]))

        if isinstance(rule[0], int):
            replace = rules[rule[0]]

            if isinstance(replace[0], list):
                for option in replace:
                    fringe.append((msg, [*option, *rule[1:]]))
            elif isinstance(replace[0], str):
                fringe.append((msg, [replace, *rule[1:]]))
            else:
                fringe.append((msg, [*replace, *rule[1:]]))

    return False


def parse_rule(line):
    i, pattern = line.split(': ')
    if '|' in pattern:
        rule = [[int(n) for n in rule.split(' ')]
                for rule in pattern.split(' | ')]
    elif '"' in pattern:
        rule = pattern[1:-1]
    else:
        rule = [int(n) for n in pattern.split(' ')]
    return int(i), rule


def load_input(replace=False):
    with open('input.txt') as f:
        rules, messages = f.read().split('\n\n')
        if replace:
            rules = rules.replace('8: 42', '8: 42 | 42 8')
            rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
        return (
            dict(map(parse_rule, rules.splitlines())),
            messages.splitlines())


if __name__ == '__main__':
    rules, messages = load_input()
    print('part 1:', sum(is_valid(msg, rules) for msg in messages))

    rules, messages = load_input(True)
    print('part 2:', sum(is_valid(msg, rules) for msg in messages))

