"""Day 22: Crab Combat"""


class Deck:
    def __init__(self, cards):
        self.cards = cards.copy()

    @property
    def size(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop(0)

    def append(self, *cards):
        self.cards.extend(cards)

    def copy(self):
        return Deck(self.cards.copy())

    def subset(self, size):
        return Deck(self.cards[:size].copy())

    def score(self):
        return sum([(i+1) * card for i, card in enumerate(reversed(self.cards))])

    def __len__(self):
        return len(self.cards)

    def __hash__(self):
        return hash(''.join(map(str, self.cards)))


def combat(deck1, deck2):
    while deck1 and deck2:
        card1, card2 = deck1.deal(), deck2.deal()

        if card1 > card2:
            deck1.append(card1, card2)
        else:
            deck2.append(card2, card1)

    return deck1, deck2


def recursive_combat(deck1, deck2):
    cache1 = set()
    cache2 = set()

    while True:
        if deck1 in cache1 and deck2 in cache2:
            return deck1, []

        if deck1.size == 0 or deck2.size == 0:
            return deck1, deck2

        cache1.add(deck1)
        cache2.add(deck2)

        card1 = deck1.deal()
        card2 = deck2.deal()

        if deck1.size >= card1 and deck2.size >= card2:
            p1, _ = recursive_combat(deck1.subset(card1), deck2.subset(card2))

            if p1.size > 0:
                deck1.append(card1, card2)
            else:
                deck2.append(card2, card1)
        elif card1 > card2:
            deck1.append(card1, card2)
        else:
            deck2.append(card2, card1)


if __name__ == '__main__':
    with open('player1.txt') as f:
        player1 = Deck([int(n) for n in f.readlines()])

    with open('player2.txt') as f:
        player2 = Deck([int(n) for n in f.readlines()])

    p1, p2 = combat(player1.copy(), player2.copy())
    print('part 1:', p1.score() if p1.size > 0 else p2.score())

    p1, p2 = recursive_combat(player1.copy(), player2.copy())
    print('part 2:', p1.score() if p1.size > 0 else p2.score())
