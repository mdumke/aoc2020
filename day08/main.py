"""Day 8: Handheld Halting"""

import re


def run(prog) -> (bool, int):
    """return (halted, accumulator)"""
    accum, ip = 0, 0
    cache = set()

    def step(accum, ip, op, n):
        if op == 'jmp': return accum, ip + n
        if op == 'acc': return accum + n, ip + 1
        return accum, ip + 1

    while ip not in cache and ip < len(prog):
        cache.add(ip)
        accum, ip = step(accum, ip, *prog[ip])

    return ip == len(prog), accum


def repair(prog) -> int:
    """return accumulator after halting"""
    for i, (op, n) in enumerate(prog):
        if op == 'acc':
            continue

        alt_op = 'nop' if op == 'jmp' else 'jmp'
        halted, accum = run([*prog[:i], (alt_op, n), *prog[i+1:]])

        if halted:
            return accum


if __name__ == '__main__':
    with open('input.txt') as f:
          prog = [(l[:3], int(l[4:])) for l in f.read().splitlines()]

    print('part 1:', run(prog)[1])
    print('part 2:', repair(prog))
