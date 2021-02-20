from functools import reduce
from operator import abs, getitem


def keep_truthful(items):
    return filter(None, items)


def abs_sum(list_nums):
    return sum(map(abs, list_nums))


def walk(data, path):
    return reduce(getitem, path, data)
