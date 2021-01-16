import math


def make_segment(point1, point2):
    return {"begin_point": point1, "end_point": point2}


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]


def is_parallel_with_x(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    return get_y(begin_point) == get_y(end_point)


def is_parallel_with_y(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    return get_x(begin_point) == get_x(end_point)
# В этой задаче, тесты написаны для отрезков, которые в
# свою очередь используют точки. Ваша задача, реализовать
# интерфейсные функции для работы с точками. Внутреннее
# представление точек должно быть основано на полярной системе
# координат, хотя интерфейс предполагает работу с декартовой
# системой (снаружи).
#
# src/points.py
# Реализуйте интерфейсные функции точек:
#
# make_decart_point. Принимает на вход координаты и возвращает
# точку. Уже реализован.
# get_x
# get_y
# >>> x = 4
# >>> y = 8
#
# # point хранит в себе данные в полярной системе координат
# >>> point = make_decart_point(x, y)
#
# # Здесь происходит преобразование из полярной в декартову
# >>> get_x(point)
# 4
# >>> get_y(point)
# 8


def make_decart_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


# BEGIN (write your solution here)
def get_x(point):
    return point['radius'] * math.cos(point['angle'])


def get_y(point):
    return point['radius'] * math.sin(point['angle'])
# END


if __name__ == '__main__':
    point1 = make_decart_point(3, 2)
    point2 = make_decart_point(0, 0)
    point3 = make_decart_point(3, -5)
    assert is_parallel_with_y(make_segment(point1, point2)) is False
    assert is_parallel_with_y(make_segment(point1, point3)) is True
    assert is_parallel_with_x(make_segment(point2, point3)) is False
