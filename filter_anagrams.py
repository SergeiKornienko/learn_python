# Реализуйте функцию filter_anagrams, которая находит все слова-анаграммы.
# Функция принимает исходное слово и последовательность (iterable) слов
# для проверки, а возвращает последовательность анаграмм.
#
# Я использовал в абзаце "слова" только для краткости. Строго говоря,
# ваша функция должна уметь находить анаграммы любых последовательностей,
# в том числе списков и кортежей. То есть решение должно быть максимально общим.
#
# Примеры
# >>> list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# ['aabb', 'bbaa']
# >>> list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# ['carer', 'racer']
# >>> list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
# []
# >>> list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))
# [[2, 1], [1, 2]]
from itertools import permutations
from collections import Counter


def filter_anagrams(elem, items):
    return filter(lambda item: Counter(elem) == Counter(item), items)


if __name__ == '__main__':
    empty = ''
    assert list(filter_anagrams(empty, [empty, 'foo', empty])) == [empty, empty]
    assert list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])) == []
    assert list(filter_anagrams(
        'abba', ['aabb', 'abcd', 'bbaa', 'dada'],
    )) == ['aabb', 'bbaa']
    assert list(filter_anagrams(
        'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
    )) == ['carer', 'racer']
    assert list(filter_anagrams((), [(), ()])) == [(), ()]
    tri = (1, 2, 3)
    irt = tuple(reversed(tri))
    assert list(filter_anagrams(
        tri, [tri, irt, tri + (4,)],
    )) == [tri, irt]
    assert list(filter_anagrams('bob', ['boo', 'bo', 'obbo'])) == []
    sample = tuple('abcd')
    sample_permutations = list(permutations(sample))
    # ^ [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ...
    # ...('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
    assert len(list(filter_anagrams(
        sample, sample_permutations,
    ))) == len(sample_permutations)
