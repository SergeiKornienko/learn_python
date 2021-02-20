from functions.remove_first_level import remove_first_level


def test_flatten():
    assert remove_first_level([]) == []
    assert remove_first_level([1, 100, 3]) == []
    assert remove_first_level([
        [1, [3, 2]],
        2,
        [3, 5],
        2,
        [130, [1, [550, 10]]],
    ]) == [1, [3, 2], 3, 5, 130, [1, [550, 10]]]
