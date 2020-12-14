"""Day 14: Docking Data"""

import re
from itertools import zip_longest, product

def parse_line(l):
    op, val = l.split(' = ')
    if op == 'mask':
        return op, val
    else:
        return int(re.findall(r'(\d+)', op)[0]), bin(int(val))[2:]


def process_part1(prog):
    mask = ''
    memory = {}

    for op, val in prog:
        if op == 'mask':
            mask = val
        else:
            memory[op] = int(''.join(reversed([digit if m == 'X' else m for m, digit in zip_longest(mask[::-1], val[::-1], fillvalue='0')])), base=2)

    return sum(memory.values())

def decode_address(addr, mask):
    floating = [i for i, char in enumerate(mask) if char == 'X']
    masked_addr = [m if m in ['1', 'X'] else digit
            for m, digit in zip_longest(mask[::-1], bin(addr)[2:][::-1], fillvalue='0')][::-1]

    for bits in product(['0', '1'], repeat=len(floating)):
        for position, bit in zip(floating, bits):
            masked_addr[int(position)] = bit
        yield ''.join(masked_addr)


def process_part2(prog):
    mask = ''
    memory = {}

    for op, val in prog:
        if op == 'mask':
            mask = val
        else:
            for address in decode_address(op, mask):
                memory[int(address, 2)] = int(val, 2)

    return sum(memory.values())

if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [parse_line(l) for l in f.read().splitlines()]

    print('part 1:', process_part1(prog))
    print('part 2:', process_part2(prog))
