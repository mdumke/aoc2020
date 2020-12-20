"""Day 20: Jurassic Jigsaw"""

import re
import numpy as np
from collections import defaultdict

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3


class Image:
    def __init__(self, img_id, data):
        self.id = img_id
        self.data = data

    @staticmethod
    def from_input(lines):
        return Image(
            int(re.split(r'[ :]', lines[0])[1]),
            np.array([list(l) for l in lines[1:]]))

    @property
    def borders(self):
        # top, right, bottom, left
        return [
            ''.join(self.data[0, :]),
            ''.join(self.data[:, -1]),
            ''.join(self.data[-1, :]),
            ''.join(self.data[:, 0])]

    def variations(self):
        data = self.data.copy()
        for _ in range(4):
            data = np.rot90(data)
            yield Image(self.id, data)
        data = np.flip(data, axis=0)
        for _ in range(4):
            data = np.rot90(data)
            yield Image(self.id, data)

    def algin_borders(self, border, target_position):
        for img in self.variations():
            if img.borders[target_position] == border:
                return img


def get_adjacent_positions(x, y, img):
    return zip([(x, y+1), (x+1, y), (x, y-1), (x-1, y)], zip(img.borders, [BOTTOM, LEFT, TOP, RIGHT]))


def build_lookup_by_border(images):
    lookup = defaultdict(list)
    for img in images:
        for border in img.borders:
            lookup[border].append(img)
    return lookup


def to_matrix(img_lookup):
    (min_x, min_y), (max_x, max_y) = min(img_lookup), max(img_lookup)
    matrix = []

    for y in range(max_y, min_y-1, -1):
        new_row = []
        for x in range(min_x, max_x + 1):
            new_row.append(img_lookup[(x, y)])
        matrix.append(new_row)

    return matrix


def build_grid(start_img, images):
    available_images = build_lookup_by_border(images)

    x, y = 0, 0
    processed = {start_img.id}
    grid = {(x, y): start_img}

    open_positions = [*get_adjacent_positions(x, y, start_img)]

    while open_positions:
        (x, y), (border, border_position) = open_positions.pop()

        neighbors = [img for img in available_images.get(
            border, []) if img.id not in processed]

        if not neighbors:
            neighbors = [img for img in available_images.get(
                border[::-1], []) if img.id not in processed]

        if not neighbors:
            continue

        neighbor = neighbors[0]
        neighbor = neighbor.algin_borders(border, border_position)
        processed.add(neighbor.id)
        grid[(x, y)] = neighbor
        open_positions.extend(get_adjacent_positions(x, y, neighbor))

    return to_matrix(grid)


def to_image(tile_matrix):
    return np.concatenate([np.concatenate([img.data[1:-1, 1:-1] for img in row], axis=1)
                           for row in tile_matrix], axis=0)


def mark_monsters(image):
    monster = np.array([
        list('                  # '),
        list('#    ##    ##    ###'),
        list(' #  #  #  #  #  #   ')])

    monster_idxs = np.c_[np.where(monster == '#')]
    n_monsters = 0

    for x in range(image.shape[0] - monster.shape[0]):
        for y in range(image.shape[1] - monster.shape[1]):
            n_matches = sum(image[i, j] == '#' for i,
                            j in monster_idxs + (x, y))
            if n_matches == len(monster_idxs):
                n_monsters += 1

                for i, j in monster_idxs + (x, y):
                    image[i, j] = 'O'

    return image, n_monsters


def count_hashes_without_monster(image):
    img = image.copy()

    for _ in range(4):
        img, n_monsters = mark_monsters(img)

        if n_monsters > 0:
            return np.where(img == '#')[0].shape[0]

        img = np.rot90(img)

    img = np.flip(img)

    for _ in range(4):
        img, n_monsters = mark_monsters(img)

        if n_monsters > 0:
            return np.where(img == '#')[0].shape[0]

        img = np.rot90(img)


if __name__ == '__main__':
    with open('input.txt') as f:
        images = [Image.from_input(lines.splitlines())
                  for lines in f.read().split('\n\n')]

    grid = build_grid(images[0], images)
    print('part 1:', grid[0][0].id * grid[0]
          [-1].id * grid[-1][0].id * grid[-1][-1].id)

    final = to_image(grid)
    print('part 2:', count_hashes_without_monster(final))
