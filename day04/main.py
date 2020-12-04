"""Day 4: Passport Processing"""

import re


format_checks = {
    'byr': lambda y: re.match(r'^\d{4}$', y) and 1920 <= int(y) <= 2002,
    'iyr': lambda y: re.match(r'^\d{4}$', y) and 2010 <= int(y) <= 2020,
    'eyr': lambda y: re.match(r'^\d{4}$', y) and 2020 <= int(y) <= 2030,
    'hcl': lambda c: re.match(r'^#[a-f0-9]{6}$', c),
    'ecl': lambda e: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', e),
    'pid': lambda p: re.match(r'^0*', p) and re.match(r'[0-9]{9}$', p),
    'hgt': lambda h: re.match(r'^(\d+)(?:cm|in)', h) and (
        (150 <= int(h[:-2]) <= 193) if (h[-2:] == 'cm') else (59 <= int(h[:-2]) <= 76))}


def is_valid_passport_basic(p):
    return len(p) == 8 or (len(p) == 7 and 'cid' not in p.keys())


def is_valid_passport(p):
    return (
        is_valid_passport_basic(p) and
        sum([bool(format_checks[k](v)) for k, v in p.items() if k != 'cid']) == 7)


if __name__ == '__main__':
    with open('input.txt') as f:
        passports = [dict(re.findall(r'(\w{3}):(\S+)', p))
                     for p in f.read().split('\n\n')]

    print('part 1:', sum(map(is_valid_passport_basic, passports)))
    print('part 2:', sum(map(is_valid_passport, passports)))
