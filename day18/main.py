
def find_main_operator(formula):
    depth = 0
    for i, symbol in enumerate(reversed(formula)):
        if symbol == '(':
            depth += 1
        if symbol == ')':
            depth -= 1
        if symbol in '+*' and depth == 0:
            return len(formula) - i - 1


def evaluate(formula):
    if formula.isdigit():
        return int(formula)

    op_idx = find_main_operator(formula)

    if op_idx is None:
        return evaluate(formula[1:-1])
    elif formula[op_idx] == '+':
        return evaluate(formula[:op_idx]) + evaluate(formula[op_idx+1:])
    else:
        return evaluate(formula[:op_idx]) * evaluate(formula[op_idx+1:])


if __name__ == '__main__':
    with open('input.txt') as f:
        formulas = [l.replace(' ', '') for l in f.read().splitlines()]

    print('part 1:', sum(evaluate(f) for f in formulas))
