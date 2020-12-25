"""Day 25: Combo Breaker"""


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


if __name__ == '__main__':
    card_key = 15628416
    door_key = 11161639

    print(transform(door_key, find_loop_size(card_key)))
