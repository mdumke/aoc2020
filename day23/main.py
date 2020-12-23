"""Day 23: Crab Cups"""

from more_itertools import pairwise


def as_sequence(cups, start):
    """return cups as list starting from given value"""
    processed = set()
    sequence = []
    current = start

    while current not in processed:
        sequence.append(current)
        processed.add(current)
        current = cups[current]

    return sequence


def move(cups, current, max_n):
    """return new current cup after one move, mutates cups"""
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


def play_game(numbers, advanced=False):
    """return final constellation of cups, starting from cup 1"""
    if advanced:
        numbers.extend(range(max(numbers)+1, 1000001))

    cups = dict(pairwise(numbers))
    cups[numbers[-1]] = numbers[0]

    current = numbers[0]
    max_n = max(numbers)

    for _ in range(10000000 if advanced else 100):
        current = move(cups, current, max_n)

    return as_sequence(cups, 1)


if __name__ == '__main__':
    numbers = [2, 4, 7, 8, 1, 9, 3, 5, 6]

    cups = play_game(numbers)
    print('part 1:', cups[1:])

    cups = play_game(numbers, True)
    print('part 2:', cups[1] * cups[2])
