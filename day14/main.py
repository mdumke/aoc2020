"""Day 14: Docking Data"""

import re
from itertools import zip_longest, product


def mask_value(val, mask):
    return int(''.join([digit if m == 'X' else m
                        for m, digit in zip_longest(mask[::-1], val[::-1], fillvalue='0')][::-1]), 2)


def process_part1(prog):
    mask = ''
    memory = {}
    for op, val in prog:
        if op == 'mask':
            mask = val
        else:
            memory[op] = mask_value(val, mask)
    return sum(memory.values())


def decode_address(addr, mask):
    addr = bin(addr)[2:]
    floating = [i for i, char in enumerate(mask) if char == 'X']
    masked_addr = [m if m in ['1', 'X'] else digit
                   for m, digit in zip_longest(mask[::-1], addr[::-1], fillvalue='0')][::-1]

    for bits in product(['0', '1'], repeat=len(floating)):
        for index, bit in zip(floating, bits):
            masked_addr[index] = bit
        yield int(''.join(masked_addr), 2)


def process_part2(prog):
    mask = ''
    memory = {}
    for op, val in prog:
        if op == 'mask':
            mask = val
        else:
            for address in decode_address(op, mask):
                memory[address] = int(val, 2)
    return sum(memory.values())


def parse_line(l):
    op, val = l.split(' = ')
    if op == 'mask':
        return op, val
    else:
        return int(re.findall(r'\d+', op)[0]), bin(int(val))[2:]


if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [parse_line(l) for l in f.read().splitlines()]

    print('part 1:', process_part1(prog))
    print('part 2:', process_part2(prog))
