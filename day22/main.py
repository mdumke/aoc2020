def play_combat(player1, player2):
    while player1 and player2:
        a, b = player1.pop(0), player2.pop(0)

        if a > b:
            player1.extend([a, b])
        else:
            player2.extend([b, a])

    return player1 if player1 else player2


def score(deck):
    return sum([(i+1) * card for i, card in enumerate(reversed(deck))])


if __name__ == '__main__':
    with open('player1.txt') as f:
        player1 = list(map(int, f.readlines()))

    with open('player2.txt') as f:
        player2 = list(map(int, f.readlines()))

    print('part 1:', score(play_combat(player1, player2)))

