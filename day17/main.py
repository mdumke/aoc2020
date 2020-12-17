import numpy as np

def coords_3d(grid, padding=1):
    max_i, max_j, max_k = grid.shape
    for i in range(-padding, max_i+padding):
        for j in range(-padding, max_j+padding):
            for k in range(-padding, max_k+padding):
                yield(i, j, k)


def is_valid_coord(i, j, k, shape):
    return (0 <= i < shape[0]) and (0 <= j < shape[1]) and (0 <= k < shape[2])


def get_boxes(grid):
    for i, j, k in coords_3d(grid):
        if is_valid_coord(i, j, k, grid.shape):
            store = grid[i, j, k]
            grid[i, j, k] = 0

        box = grid[max(0,i-1):i+2, max(0,j-1):j+2, max(0,k-1):k+2].copy()
        is_active = store if is_valid_coord(i, j, k, grid.shape) else 0

        if is_valid_coord(i, j, k, grid.shape):
            grid[i, j, k] = store

        yield(i, j, k, is_active, box)


def iterate(grid):
    new_grid = np.zeros(np.array(grid.shape) + (2, 2, 2))

    for i, j, k, is_active, box in get_boxes(grid):
        if is_active:
            new_grid[i+1, j+1, k+1] = box.sum() in [2, 3]
        else:
            new_grid[i+1, j+1, k+1] = box.sum() == 3

    return new_grid



if __name__ == '__main__':
    with open('input.txt') as f:
        grid = np.array([[symbol == '#' for symbol in line] for line in f.read().splitlines()])[None]

    for _ in range(6):
        grid = iterate(grid)

    print('part 1:', int(grid.sum()))
