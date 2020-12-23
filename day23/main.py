"""Day 23: Crab Cups"""

from more_itertools import pairwise


def as_sequence(cups: dict, start: int) -> list:
    """return cups as list starting *after* given value"""
    seq = []
    current = cups[start]
    while current != start:
        seq.append(current)
        current = cups[current]
    return seq


def move(cups: dict, current: int, max_n: int) -> int:
    """return new current cup after one move, mutates cups"""
    # extract sub-sequence to move around
    tmp = (cups[current],
           cups[cups[current]],
           cups[cups[cups[current]]])

    # find cup to insert after
    target = (current - 1) % max_n
    while target in tmp or target == 0:
        target = (target - 1) % (max_n + 1)

    # rewire cups to insert tmp sequence
    cups[current] = cups[tmp[-1]]
    cups[tmp[-1]] = cups[target]
    cups[target] = tmp[0]

    return cups[current]


def play_game(numbers: list, rounds: int) -> list:
    """return final constellation of cups, starting from cup 1"""
    # build cups dict {cup: next-cup}
    cups = dict(pairwise(numbers))
    cups[numbers[-1]] = numbers[0]
    current = numbers[0]
    max_n = max(numbers)

    for _ in range(rounds):
        current = move(cups, current, max_n)

    return as_sequence(cups, 1)


if __name__ == '__main__':
    numbers = [2, 4, 7, 8, 1, 9, 3, 5, 6]

    cups = play_game(numbers, 100)
    print('part 1:', cups)

    numbers.extend(range(max(numbers)+1, 1000001))
    cups = play_game(numbers, 10000000)
    print('part 2:', cups[0] * cups[1])
