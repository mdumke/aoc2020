def find_loop_size(key):
    value = 1
    loop = 0
    while True:
        loop += 1
        value = (value * 7) % 20201227
        if value == key:
            return loop

def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


def find_encryption_key(key1, key2):
    return transform(key2, find_loop_size(key1))


if __name__ == '__main__':
    card_key = 15628416
    door_key = 11161639

    print('part 1:', find_encryption_key(card_key, door_key))

