"""Day 18: Operation Order"""

from operator import add, mul


def get_operator(formula, advanced):
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
            if not advanced:
                break
    return candidate


def evaluate(formula, advanced=False):
    if formula.isdigit():
        return int(formula)

    op = get_operator(formula, advanced)

    if op is None:
        return evaluate(formula[1:-1], advanced)

    return op[0](
        evaluate(formula[:op[1]], advanced),
        evaluate(formula[op[1]+1:], advanced))



if __name__ == '__main__':
    with open('input.txt') as f:
        formulas = [l.replace(' ', '') for l in f.read().splitlines()]

    print('part 1:', sum(evaluate(f) for f in formulas))
    print('part 2:', sum(evaluate(f, True) for f in formulas))
