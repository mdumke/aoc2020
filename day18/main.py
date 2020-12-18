"""Day 18: Operation Order"""

def find_main_operator(formula):
    depth = 0
    for i, symbol in enumerate(reversed(formula)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol in '+*' and depth == 0:
            return len(formula) - i - 1


def find_lowest_precedence_operator(formula):
    depth = 0
    candidate = None
    for i, symbol in enumerate(reversed(formula)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol == '*' and depth == 0:
            candidate = len(formula) - i - 1
            break
        if symbol == '+' and depth == 0:
            candidate = len(formula) - i - 1
    return candidate


def evaluate(formula, advanced=False):
    if formula.isdigit():
        return int(formula)

    if advanced:
        op_idx = find_lowest_precedence_operator(formula)
    else:
        op_idx = find_main_operator(formula)

    if op_idx is None:
        return evaluate(formula[1:-1], advanced)
    elif formula[op_idx] == '+':
        return evaluate(formula[:op_idx], advanced) + evaluate(formula[op_idx+1:], advanced)
    else:
        return evaluate(formula[:op_idx], advanced) * evaluate(formula[op_idx+1:], advanced)


if __name__ == '__main__':
    with open('input.txt') as f:
        formulas = [l.replace(' ', '') for l in f.read().splitlines()]

    print('part 1:', sum(evaluate(f) for f in formulas))
    print('part 2:', sum(evaluate(f, True) for f in formulas))
