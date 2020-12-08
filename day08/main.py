"""Day 8: Handheld Halting"""

import re


def run_program(prog) -> (bool, int):
    """return (has_inifinite_loop, accumulator)"""
    accum, i = 0, 0
    cache = set()

    while i not in cache and i < len(prog):
        cache.add(i)
        cmd, n = prog[i]
        if cmd == 'jmp':
            i += n
            continue
        if cmd == 'acc':
            accum += n
        i += 1

    return i < len(prog), accum


def repair_program(prog) -> int:
    """return accumulator at halting"""
    for i, (cmd, n) in enumerate(prog):
        if cmd == 'acc':
            continue

        alt_cmd = ('nop' if cmd == 'jmp' else 'jmp', n)
        inf_loop, accum = run_program([*prog[:i], alt_cmd, *prog[i+1:]])

        if not inf_loop:
            return accum


if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [(cmd, int(n))
                for cmd, n in re.findall(r'(\w{3}) ([+-]\d+)', f.read())]

    print('part 1:', run_program(prog)[1])
    print('part 2:', repair_program(prog))
