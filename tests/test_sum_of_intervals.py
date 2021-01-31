from functions.sum_of_intervals import sum_of_intervals


def test_sum_of_intervals():
    assert sum_of_intervals([[5, 5]]) == 0
    assert sum_of_intervals([[3, 10]]) == 7
    assert sum_of_intervals([
        [1, 2],
        [11, 12],
    ]) == 2
    assert sum_of_intervals([
        [2, 7],
        [6, 6],
    ]) == 5
    assert sum_of_intervals([
        [1, 9],
        [7, 12],
        [3, 4],
    ]) == 11
    assert sum_of_intervals([
        [1, 5],
        [1, 10],
    ]) == 9
