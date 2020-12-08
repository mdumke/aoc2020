"""Day 8: Handheld Halting"""

import re


def run_program(prog) -> (bool, int):
    """return (has_infinite_loop, accumulator)"""
    accum, i = 0, 0
    cache = set()

    while i not in cache and i < len(prog):
        cache.add(i)
        op, n = prog[i]
        if op == 'jmp':
            i += n
            continue
        if op == 'acc':
            accum += n
        i += 1

    return i < len(prog), accum


def repair_program(prog) -> int:
    """return accumulator at halting"""
    for i, (op, n) in enumerate(prog):
        if op == 'acc':
            continue

        alt_op = 'nop' if op == 'jmp' else 'jmp'
        inf_loop, accum = run_program([*prog[:i], (alt_op, n), *prog[i+1:]])

        if not inf_loop:
            return accum


if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [(op, int(n))
                for op, n in re.findall(r'(\w{3}) ([+-]\d+)', f.read())]

    print('part 1:', run_program(prog)[1])
    print('part 2:', repair_program(prog))
