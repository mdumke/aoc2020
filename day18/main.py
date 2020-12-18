"""Day 18: Operation Order"""

from operator import add, mul


def next_available(formula):
    depth = 0
    candidate = None
    for i, symbol in enumerate(reversed(formula)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol == '+' and depth == 0:
            candidate = add, len(formula) - i - 1
            break
        if symbol == '*' and depth == 0:
            candidate = mul, len(formula) - i - 1
            break
    return candidate


def lowest_precedence(formula):
    depth = 0
    candidate = None
    for i, symbol in enumerate(reversed(formula)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol == '*' and depth == 0:
            candidate = mul, len(formula) - i - 1
            break
        if symbol == '+' and depth == 0:
            candidate = add, len(formula) - i - 1
    return candidate


def evaluate(formula, get_operator):
    if formula.isdigit():
        return int(formula)

    if op := get_operator(formula):
        left = evaluate(formula[:op[1]], get_operator)
        right = evaluate(formula[op[1]+1:], get_operator)
        return op[0](left, right)
    else:
        return evaluate(formula[1:-1], get_operator)


if __name__ == '__main__':
    with open('input.txt') as f:
        formulas = [l.replace(' ', '') for l in f.read().splitlines()]

    print('part 1:', sum(evaluate(f, next_available) for f in formulas))
    print('part 2:', sum(evaluate(f, lowest_precedence) for f in formulas))
