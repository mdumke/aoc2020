def count_ingredients_without_allergenes(foods):
    candidates = {}

    for ingredients, allergenes in foods:
        for a in allergenes:
            if candidates.get(a):
                candidates[a] = candidates[a] & set(ingredients)
            else:
                candidates[a] = set(ingredients)

    combined = set()

    for ingredients in candidates.values():
        combined |= ingredients

    allergene_free = 0

    for ingredients, _ in foods:
        for i in ingredients:
            if i not in combined:
                allergene_free += 1

    return allergene_free


if __name__ == '__main__':
    with open('input.txt') as f:
        foods = [[part.replace(',', '').split(' ')
                  for part in line[:-2].split(' (contains ')] for line in f]

    print('part 1:', count_ingredients_without_allergenes(foods))
