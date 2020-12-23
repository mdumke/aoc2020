"""Day 23: Crab Cups"""

import math
from more_itertools import pairwise

def serialize(cups, start):
    done = set()
    result = []
    current = start

    while current not in done:
        result.append(current)
        done.add(current)
        current = cups[current]

    return result


def move(cups, current, max_n):
    tmp = (cups[current],
           cups[cups[current]],
           cups[cups[cups[current]]])

    cups[current] = cups[tmp[-1]]
    target = (current - 1) % max_n

    while target in tmp or target == 0:
        target = (target - 1) % (max_n + 1)

    cups[tmp[-1]] = cups[target]
    cups[target] = tmp[0]

    return cups[current]


def play_game(numbers):
    cups = dict(pairwise(numbers))
    cups[numbers[-1]] = numbers[0]

    current = numbers[0]
    max_n = max(numbers)

    for i in range(100):
        current = move(cups, current, max_n)

    return ''.join(map(str, serialize(cups, 1)[1:]))


def play_advanced_game(numbers):
    numbers = [*numbers, *list(range(max(numbers)+1, 1000001))]
    cups = dict(pairwise(numbers))
    cups[numbers[-1]] = numbers[0]

    current = numbers[0]
    max_n = max(numbers)

    for i in range(10_000_000):
        current = move(cups, current, max_n)

    return serialize(cups, 1)[1:3]


if __name__ == '__main__':
    numbers = [2, 4, 7, 8, 1, 9, 3, 5, 6]

    print('part 1:', play_game(numbers))
    print('part 2:', math.prod(play_advanced_game(numbers)))

