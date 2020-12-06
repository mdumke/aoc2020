"""Day 6: Custom Customs"""

from collections import Counter


def count_any_answered(group):
    return len(set(group.replace('\n', '')))


def count_all_answered(group):
    return sum([count == len(group.split())
                for count in Counter(group.replace('\n', '')).values()])


if __name__ == '__main__':
    with open('input.txt') as f:
        groups = f.read().split('\n\n')

    print('part 1:', sum(map(count_any_answered, groups)))
    print('part 2:', sum(map(count_all_answered, groups)))
