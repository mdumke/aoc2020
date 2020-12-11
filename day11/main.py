from itertools import product

def count_adjacent(i, j, seats):
    count =0
    for dx, dy in product([-1, 0, 1], repeat=2):
        if (dx, dy) == (0, 0):
            continue
        if not (0 <= i + dx < len(seats)):
            continue
        if not (0 <= j + dy < len(seats[0])):
            continue

        count += seats[i+dx][j+dy] == '#'

    return count


def update_seats(seats):
    new_seats = []
    n, m = len(seats), len(seats[0])

    for row in range(n):
        new_row = ''

        for col in range(m):
            if seats[row][col] == '.':
                new_row += '.'
            else:
                adjacent = count_adjacent(row, col, seats)

                if seats[row][col] == 'L' and adjacent == 0:
                    new_row += '#'
                elif seats[row][col] == '#' and adjacent >= 4:
                    new_row += 'L'
                else:
                    new_row += seats[row][col]

        new_seats.append(new_row)

    return new_seats


def find_final_seats(seats):
    while True:
        new_seats = update_seats(seats)

        if ''.join(seats) == ''.join(new_seats):
            return new_seats

        seats = new_seats


def count_occupied(seats):
    return sum([s == '#' for row in seats for s in row])

def zero_matrix(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def is_valid_position(x, y, seats):
    return (0 <= x < len(seats)) and (0 <= y < len(seats[0]))

def rotate(matrix):
    return list(list(l[::-1]) for l in zip(*matrix))

def checksum(seats):
    return hash(''.join([''.join(l) for l in seats]))

def diagonal_trace(seats, counts) -> None:
    def diagonal(x, y):
        while is_valid_position(x, y, seats):
            yield (x, y)
            x, y = x + 1, y + 1

    for row in range(len(seats)):
        last_seat = '.'

        for i, j in diagonal(row, 0):
            counts[i][j] += last_seat == '#'

            if seats[i][j] != '.':
                last_seat = seats[i][j]

    for col in range(1, len(seats[0])):
        last_seat = '.'

        for i, j in diagonal(0, col):
            counts[i][j] += last_seat == '#'

            if seats[i][j] != '.':
                last_seat = seats[i][j]


def horizontal_trace(seats, counts) -> None:
    for i, row in enumerate(seats):
        last_seat = '.'

        for j, current in enumerate(row):
            counts[i][j] += last_seat == '#'

            if current != '.':
                last_seat = seats[i][j]


def part2(seats):
    while True:
        counts = zero_matrix(len(seats), len(seats[0]))

        horizontal_trace(seats, counts)
        diagonal_trace(seats, counts)

        seats, counts = rotate(seats), rotate(counts)
        horizontal_trace(seats, counts)
        diagonal_trace(seats, counts)

        seats, counts = rotate(seats), rotate(counts)
        horizontal_trace(seats, counts)
        diagonal_trace(seats, counts)

        seats, counts = rotate(seats), rotate(counts)
        horizontal_trace(seats, counts)
        diagonal_trace(seats, counts)

        seats, counts = rotate(seats), rotate(counts)
        counts

        new_seats = []

        for i, row in enumerate(seats):
            new_row = []

            for j, seat in enumerate(row):
                if seat == 'L' and counts[i][j] == 0:
                    new_seat = '#'
                elif seat == '#' and counts[i][j] >= 5:
                    new_seat = 'L'
                else:
                    new_seat = seat

                new_row.append(new_seat)

            new_seats.append(new_row)

        if checksum(seats) == checksum(new_seats):
            return new_seats

        seats = new_seats


if __name__ == '__main__':
    with open('input.txt') as f:
            seats = f.read().splitlines()

    print('part 1:', count_occupied(find_final_seats(seats)))
    print('part 2:', count_occupied(part2(seats)))
