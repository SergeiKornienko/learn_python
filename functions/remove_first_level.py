import itertools


def remove_first_level(tree):
    children = filter(lambda elem: isinstance(elem, list), tree)
    return list(itertools.chain(*children))
