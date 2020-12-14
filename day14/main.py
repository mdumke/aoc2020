import re
from itertools import zip_longest

def parse_line(l):
    op, val = l.split(' = ')
    if op == 'mask':
        return op, val
    else:
        return int(re.findall(r'(\d+)', op)[0]), bin(int(val))[2:]

with open('input.txt') as f:
    prog = [parse_line(l) for l in f.read().splitlines()]

mask = ''
memory = {}

for op, val in prog:
    if op == 'mask':
        mask = val
    else:
        memory[op] = int(''.join(reversed([digit if m == 'X' else m for m, digit in zip_longest(mask[::-1], val[::-1], fillvalue='0')])), base=2)

print('part 1:', sum(memory.values()))
