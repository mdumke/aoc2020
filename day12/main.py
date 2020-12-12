import re

with open('input.txt') as f:
    instructions = [(op, int(n)) for op, n in re.findall('(\w)(\d+)', f.read())]

def forward(n, orientation, position):
    if orientation == 'N':
        return (position[0], position[1] + n)
    if orientation == 'S':
        return (position[0], position[1] - n)
    if orientation == 'E':
        return (position[0] + n, position[1])
    if orientation == 'W':
        return (position[0] - n, position[1])

    raise Error('unknown orientation')


def rotate(orientation, op, n):
    left = dict(E='N', S='E', W='S', N='W')
    right = dict(E='S', S='W', W='N', N='E')
    flip = dict(E='W', W='E', N='S', S='N')

    if n == 90:
        if op == 'L':
            return left[orientation]
        if op == 'R':
            return right[orientation]

    if n == 180:
        return flip[orientation]

    if n == 270:
        if op == 'R':
            return left[orientation]
        if op == 'L':
            return right[orientation]

    raise Error('unknown orientation', op, n, orientation)


position = (0, 0)
orientation = 'E'

for op, n in instructions:
    if op == 'F':
        position = forward(n, orientation, position)
    elif op == 'L':
        orientation = rotate(orientation, op, n)
    elif op == 'R':
        orientation = rotate(orientation, op, n)
    elif op == 'N':
        position = (position[0], position[1] + n)
    elif op == 'S':
        position = (position[0], position[1] - n)
    elif op == 'E':
        position = (position[0] + n, position[1])
    elif op == 'W':
        position = (position[0] - n, position[1])
    else:
        raise Error('unknwon op')


print('part 1:', abs(position[0]) + abs(position[1]))
