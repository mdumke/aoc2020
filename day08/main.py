"""Day 8: Handheld Halting"""

import re


def run_program(prog) -> (bool, int):
    """return (halted, accumulator)"""
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

    return i == len(prog), accum


def repair_program(prog) -> int:
    """return accumulator after halting"""
    for i, (op, n) in enumerate(prog):
        if op == 'acc':
            continue

        alt_op = 'nop' if op == 'jmp' else 'jmp'
        halted, accum = run_program([*prog[:i], (alt_op, n), *prog[i+1:]])

        if halted:
            return accum


if __name__ == '__main__':
    with open('input.txt') as f:
          prog = [(l[:3], int(l[4:])) for l in f.read().splitlines()]

    print('part 1:', run_program(prog)[1])
    print('part 2:', repair_program(prog))
