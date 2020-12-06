"""Day 5: Binary Boarding"""


def get_seat_ids():
    with open('input.txt') as f:
        return [
            int(line[:7].replace('B', '1').replace('F', '0'), base=2) * 8 +
            int(line[7:].replace('R', '1').replace('L', '0'), base=2)
            for line in f.read().splitlines()]


def find_missing(values):
    i, offset = 0, values[0]
    while i < len(values):
        if values[i] != offset + i:
            return offset + i
        i += 1


if __name__ == '__main__':
    seats = get_seat_ids()
    print('part 1:', max(seats))
    print('part 2:', find_missing(sorted(seats)))
