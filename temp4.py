from collections import defaultdict


with open('./input4.txt') as f:
    data = filter(bool, f.readlines())


def old_is_nice(s):
    bad_combos = ['ab', 'cd', 'pq', 'xy']
    if any([x in s for x in bad_combos]):
        return False
    vowels = list("aeiou")
    num_vowels = 0
    prev_char = None
    contains_streak = False
    for char in s:
        print char, num_vowels
        if char in vowels:
            num_vowels += 1
        if char == prev_char:
            contains_streak = True
        prev_char = char

    if num_vowels < 3:
        return False

    if not contains_streak:
        return False

    return True

def is_nice(s):
    """
    >>> is_nice('qjhvhtzxzqqjkmpb')
    True
    >>> is_nice('xxyxx')
    True
    >>> is_nice('uurcxstgmygtbstg')
    False
    >>> is_nice('ieodomkazucvgmuy')
    False
    """
    pairs = zip(s, s[1:])
    is_pairs_found = False
    for idx, pair in enumerate(pairs):
        if pair in pairs[:idx][:-1] + pairs[idx + 2:]:
            is_pairs_found = True
            break

    if not is_pairs_found:
        return False

    for triple in zip(s, s[1:], s[2:]):
        if triple[0] == triple[-1]:
            return True
    return False



if __name__ == '__main__':
    count = 0
    for s in data:
        if is_nice(s):
            count += 1
    print count

