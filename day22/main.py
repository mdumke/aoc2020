"""Day 22: Crab Combat"""


class Deck(list):
    def copy(self):
        return Deck(super(Deck, self).copy())

    def __getitem__(self, idx):
        return Deck(super(Deck, self).__getitem__(idx))

    def __hash__(self):
        return hash(''.join(map(str, self)))


def combat(deck1, deck2):
    while deck1 and deck2:
        card1, card2 = deck1.pop(0), deck2.pop(0)

        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])

    return deck1, deck2


def recursive_combat(deck1, deck2):
    cache1 = set()
    cache2 = set()

    while True:
        if deck1 in cache1 and deck2 in cache2:
            return deck1, []

        if not deck1 or not deck2:
            return deck1, deck2

        cache1.add(deck1)
        cache2.add(deck2)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            p1, _ = recursive_combat(
                deck1[:card1].copy(),
                deck2[:card2].copy())

            if p1:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])
        elif card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])


def score(deck):
    return sum([(i+1) * card for i, card in enumerate(reversed(deck))])


def load_deck(file):
    with open(file) as f:
        return Deck(map(int, f.readlines()))


if __name__ == '__main__':
    player1 = load_deck('player1.txt')
    player2 = load_deck('player2.txt')

    p1, p2 = combat(player1.copy(), player2.copy())
    print('part 1:', score(p1 if p1 else p2))

    p1, p2 = recursive_combat(player1.copy(), player2.copy())
    print('part 2:', score(p1 if p1 else p2))
