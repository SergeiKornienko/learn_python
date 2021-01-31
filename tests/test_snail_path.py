from functions.snail_path import snail_path


def test_snail_path():
    assert not snail_path([])



    assert snail_path([[0]]) == [0]

    assert snail_path([[1, 2, 3]]) == [1, 2, 3]

    assert snail_path([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    assert snail_path([
        [1, 2],
        [3, 4],
    ]) == [1, 2, 4, 3]

    assert snail_path([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    assert snail_path([
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]) == [None, 0, True, False, object, 'foo', [], -1, '']

    assert snail_path([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert not snail_path([[]])
