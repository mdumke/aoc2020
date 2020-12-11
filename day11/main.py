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


if __name__ == '__main__':
    with open('input.txt') as f:
            seats = f.read().splitlines()

    print('part 1:', count_occupied(find_final_seats(seats)))
