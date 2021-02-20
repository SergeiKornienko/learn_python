from functions.flatten import flatten


def test_flatten():
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
