def find_target(cups, current):
    candidate = current-1

    while candidate > 0:
        if candidate in cups:
            return cups.index(candidate)
        candidate -= 1

    return cups.index(max(cups))


def move(cups):
    tmp = [*cups[4:], cups[0]]
    target = find_target(tmp, cups[0])
    return [*tmp[:target+1], *cups[1:4], *tmp[target+1:]]


def find_final_constellation(cups, epochs):
    for _ in range(epochs):
        cups = move(cups)
    return cups


def cups_after_1(cups):
    one = cups.index(1)
    return ''.join(map(str, [*cups[one+1:], *cups[:one]]))


if __name__ == '__main__':
    cups = list(map(int, '247819356'))

    print('part 1:', cups_after_1(find_final_constellation(cups, 100)))
