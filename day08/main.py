"""Day 8: Handheld Halting"""

import re


def run_program(prog):
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

    return accum, i == len(prog)


def repair_program(prog):
    for i, (cmd, n) in enumerate(prog):
        if cmd == 'acc':
            continue

        accum, halts = run_program(
            [*prog[:i], ('nop' if cmd == 'jmp' else 'jmp', n), *prog[i+1:]])

        if halts:
            return accum


if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [(cmd, int(n))
                for cmd, n in re.findall(r'(\w{3}) ([+-]\d+)', f.read())]

    print('part 1:', run_program(prog)[0])
    print('part 2:', repair_program(prog))
