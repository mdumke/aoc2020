import re
import numpy as np
from collections import defaultdict

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

class Image:
    def __init__(self, raw):
        self.id = int(re.split(r'[ :]', raw[0])[1])
        self.data = np.array([list(l) for l in raw[1:]])

    @property
    def borders(self):
        # top, right, bottom left
        return [
            ''.join(self.data[0, :]),
            ''.join(self.data[:, -1]),
            ''.join(self.data[-1, :]),
            ''.join(self.data[:, 0])]

    def transform(self, border, target_position):
        for _ in range(4):
            if self.borders[target_position] == border:
                return
            self.data = np.rot90(self.data)

        self.data = np.flip(self.data, axis=0)

        for _ in range(4):
            if self.borders[target_position] == border:
                return
            self.data = np.rot90(self.data)

    def __repr__(self):
        return str(self.id)


def get_adjacent_positions(x, y, img):
    return zip([(x, y+1), (x+1, y), (x, y-1), (x-1, y)], zip(img.borders, [BOTTOM, LEFT, TOP, RIGHT]))

def build_lookup_by_border(images):
    lookup = defaultdict(list)
    for img in images:
        for border in img.borders:
            lookup[border].append(img)
    return lookup

def build_grid(start_img, images):
    available_images = build_lookup_by_border(images)

    x, y = 0, 0
    fixed_positions = {start_img.id: (x, y)}
    open_positions = [*get_adjacent_positions(x, y, start_img)]

    while open_positions:
        (x, y), (border, border_position) = open_positions.pop()

        neighbors = [img for img in available_images.get(border, []) if img.id not in fixed_positions]

        if not neighbors:
            neighbors = [img for img in available_images.get(border[::-1], []) if img.id not in fixed_positions]

        if not neighbors:
            continue

        neighbor = neighbors[0]
        neighbor.transform(border, border_position)
        fixed_positions[neighbor.id] = (x, y)
        open_positions.extend(get_adjacent_positions(x, y, neighbor))

    return {pos: _id for _id, pos in fixed_positions.items()}


def part1(images):
    grid = build_grid(images[0], images)
    (min_x, min_y), (max_x, max_y) = min(grid), max(grid)

    result = []

    for x in range(min_x, max_x + 1):
        new_row = []
        for y in range(min_y, max_y + 1):
            new_row.append(grid[(x, y)])
        result.append(new_row)

    return result[0][0] * result[0][-1] * result[-1][0] * result[-1][-1]

if __name__ == '__main__':
    with open('input.txt') as f:
        image_data = [l.splitlines() for l in f.read().split('\n\n')]
        images = [Image(line) for line in image_data]

    print('part 1:', part1(images))

