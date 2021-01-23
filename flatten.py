# Реализуйте функцию flatten, которая делает
# плоским вложенный список.
#
# Примеры
# >>> from solution import flatten
# >>> flatten([])
# []
# >>> flatten([2, [3, 5], [[4, 3], 2]])
# [2, 3, 5, 4, 3, 2]
# >>>
# BEGIN (write your solution here)
def flatten(items):
    new_list = []
    for item in items:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list
# END


if __name__ == '__main__':
    assert flatten([]) == []
    assert flatten([
        1,
        2,
        [3, 5],
        [[4, 3], 2],
    ]) == [1, 2, 3, 5, 4, 3, 2]
    assert flatten([
        [1, [5], [], [[-3, 'hi']]],
        'string',
        10,
        [[[5]]],
    ]) == [1, 5, -3, 'hi', 'string', 10, 5]
    assert flatten([
        1,
        2,
        {'a': 1},
        [3, 5],
        2,
    ]) == [1, 2, {'a': 1}, 3, 5, 2]
