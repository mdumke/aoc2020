"""Day 8: Handheld Halting"""

import re


class CPU:
    def __init__(self):
        self.accumulator = 0
        self.pos = 0

    def acc(self, n):
        self.accumulator += n
        self.pos += 1

    def jmp(self, n):
        self.pos += n

    def nop(self, n):
        self.pos += 1

    def run(self, prog):
        cache = set()

        while self.pos < len(prog):
            if self.pos in cache:
                raise Exception('infinite loop')
            cache.add(self.pos)
            cmd, n = prog[self.pos]
            getattr(self, cmd)(n)

        return self.accumulator


def get_accumulator_at_halt(program):
    cpu = CPU()
    try:
        cpu.run(program)
    except:
        return cpu.accumulator


def repair_program(program):
    for i, (cmd, n) in enumerate(program):
        if cmd == 'acc':
            continue
        try:
            cpu = CPU()
            cpu.run([*prog[:i], ('nop' if cmd == 'jmp' else 'jmp', n), *prog[i+1:]])
            return cpu.accumulator
        except:
            pass


if __name__ == '__main__':
    with open('input.txt') as f:
        prog = [(cmd, int(n))
                for cmd, n in re.findall(r'(\w{3}) ([+-]\d+)', f.read())]

    print('part 1:', get_accumulator_at_halt(prog))
    print('part 2:', repair_program(prog))
