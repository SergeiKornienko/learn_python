from collections import Counter


def filter_anagrams(elem, items):
    return filter(lambda item: Counter(elem) == Counter(item), items)
