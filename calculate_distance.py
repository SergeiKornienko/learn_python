# Реализуйте функцию calculate_distance, которая находит расстояние между двумя точками на плоскости:
#
# >>> point1 = [0, 0]
# >>> point2 = [3, 4]
# >>> calculate_distance(point1, point2)
# 5.0
from math import sqrt


def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == '__main__':
    assert calculate_distance([0, 0], [3, 4]) == 5
    assert calculate_distance([-1, -4], [-1, -10]) == 6
    assert calculate_distance([1, 10], [1, 3]) == 7
