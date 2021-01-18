# В этом задании под деревом понимается любой список
# элементов, которые в свою очередь могут быть также
# деревьями (списками). Пример:
#
# [
#   3, # лист
#   [5, 3], # узел
#   [[2]] # узел
# ]
# Больше примеров в тестах.
#
# Реализуйте функцию, которая принимает на вход дерево,
# и возвращает новое, элементами которого являются
#  дети вложенных узлов.
#
# Пример
# >>> from solution import remove_first_level
# >>>
# >>> tree1 = [[5], 1, [3, 4]]
# >>> remove_first_level(tree1)
# [5, 3, 4]
# >>> tree2 = [1, 2, [3, 5], [[4, 3], 2]]
# >>> remove_first_level(tree2)
# [3, 5, [4, 3], 2]
# >>>
import itertools


def remove_first_level(tree):
    children = filter(lambda elem: isinstance(elem, list), tree)
    return list(itertools.chain(*children))


if __name__ == '__main__':
    assert remove_first_level([]) == []
    assert remove_first_level([1, 100, 3]) == []
    assert remove_first_level([
        [1, [3, 2]],
        2,
        [3, 5],
        2,
        [130, [1, [550, 10]]],
    ]) == [1, [3, 2], 3, 5, 130, [1, [550, 10]]]
