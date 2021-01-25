from functions.calculate_distance import calculate_distance


def test_points():
    assert calculate_distance([0, 0], [3, 4]) == 5
    assert calculate_distance([-1, -4], [-1, -10]) == 6
    assert calculate_distance([1, 10], [1, 3]) == 7
