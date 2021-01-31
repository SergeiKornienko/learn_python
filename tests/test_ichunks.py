from itertools import count, islice

from functions.ichunks import ichunks


def test_ichunks_with_lists():
    assert list(ichunks(1, [])) == []
    assert list(ichunks(2, [42])) == []
    assert list(ichunks(1, [100, 200])) == [[100], [200]]  # noqa: WPS221

    assert list(
        ichunks(3, ['a', 'b', 'c', 'd']),
    ) == [['a', 'b', 'c']]  # noqa: WPS221


def test_ichunks_with_iterator():
    # поток чисел "1000, 1003, 1006..."
    stream = count(1000, 3)

    assert list(
        islice(ichunks(1, stream), 3),
    ) == [[1000], [1003], [1006]]  # noqa: WPS221

    assert list(
        islice(ichunks(3, stream), 1),
    ) == [[1009, 1012, 1015]]  # noqa: WPS221

