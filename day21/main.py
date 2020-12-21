"""Day 21: Allergen Assessment"""

from operator import itemgetter
from itertools import permutations


def find_possible_ingredients(foods):
    """returns lookup {allergene: {ingredients}}"""
    candidates = {}
    for ingredients, allergenes in foods:
        for a in allergenes:
            if not candidates.get(a):
                candidates[a] = set(ingredients)
            candidates[a] = candidates[a] & set(ingredients)
    return candidates


def combine_sets(sets):
    """returns the union of given sets"""
    return sets[0].union(*sets[1:])


def count_ingredients_without_allergenes(foods):
    """returns number of ingredients that cannot contain known allergenes"""
    candidates = find_possible_ingredients(foods)
    return sum([ing not in combine_sets(list(candidates.values()))
                for ingredients, _ in foods for ing in ingredients])


def find_allergene_assignment(foods):
    """returns list of [(allergene, ingredient)]"""
    candidates = find_possible_ingredients(foods)
    combined = combine_sets(list(candidates.values()))

    for assignment in permutations(list(combined), r=len(candidates)):
        valid = True
        for allergene, ingredient in zip(candidates, assignment):
            if ingredient not in candidates[allergene]:
                valid = False
                break
        if valid:
            return list(zip(candidates, assignment))


def get_dangerous_ingredients(foods):
    """returns list of ingredients"""
    assignment = find_allergene_assignment(foods)
    return ','.join([i for a, i in sorted(assignment, key=itemgetter(0))])


if __name__ == '__main__':
    with open('input.txt') as f:
        foods = [[part.replace(',', '').split(' ')
                  for part in line[:-2].split(' (contains ')] for line in f]

    print('part 1:', count_ingredients_without_allergenes(foods))
    print('part 2:', get_dangerous_ingredients(foods))
