"""Day 19: Monster Messages"""

def is_valid(msg, rules):
    fringe = [(msg, rules[0])]

    while fringe:
        current_msg, current_rule = fringe.pop()

        if not current_msg and not current_rule:
            return True

        if not current_msg or not current_rule:
            continue

        if isinstance(current_rule[0], str):
            if current_rule[0] == current_msg[0]:
                fringe.append((current_msg[1:], current_rule[1:]))

        if isinstance(current_rule[0], int):
            replace = rules[current_rule[0]]

            if isinstance(replace[0], list):
                for option in replace:
                    fringe.append((current_msg, [*option, *current_rule[1:]]))
            elif isinstance(replace[0], str):
                fringe.append((current_msg, [replace, *current_rule[1:]]))
            else:
                fringe.append((current_msg, [*replace, *current_rule[1:]]))

    return False



def load_input(replace=False):
    to_numbers = lambda s: [int(n) for n in s.strip().split(' ')]

    def parse_rule(line):
        i, pattern = line.split(':')
        if '|' in pattern:
            rule = [to_numbers(r) for r in pattern.split('|')]
        elif '"' in pattern:
            rule = pattern.strip()[1:-1]
        else:
            rule = to_numbers(pattern)
        return int(i), rule

    with open('input.txt') as f:
        rules, messages = f.read().split('\n\n')
        if replace:
            rules = rules.replace('8: 42\n', '8: 42 | 42 8\n')
            rules = rules.replace('11: 42 31\n', '11: 42 31 | 42 11 31\n')
        rules = dict(parse_rule(line) for line in rules.splitlines())

    return rules, messages.splitlines()


if __name__ == '__main__':
    rules, messages = load_input()
    print('part 1:', sum(is_valid(msg, rules) for msg in messages))

    rules, messages = load_input(replace=True)
    print('part 2:', sum(is_valid(msg, rules) for msg in messages))

