def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]
# Отрезок — еще один графический примитив. В коде описывается парой
# точек, одна из которых — начало отрезка, другая — конец. Обычный
# отрезок не имеет направления, поэтому вы сами вольны выбирать то, какую
# точку считать началом, а какую концом.
#
# В этом задании подразумевается, что вы уже понимаете принцип построения
# абстракции и способны самостоятельно принять решение о том, как она
# будет реализована. Напомню, что сделать это можно разными способами и
# нет одного правильного.
#
# src/segments.py
# Реализуйте указанные ниже функции:
#
# make_segment. Принимает на вход две точки и возвращает отрезок.
# get_mid_point_of_segment. Принимает на вход отрезок и возвращает
# точку находящуюся на середине отрезка.
# Представление отрезка вы должны придумать сами!
#
# Пример
# >>> segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
# >>> get_mid_point_of_segment(segment)
# {'x': 1.5, 'y': 1}


def make_segment(point1, point2):
    return {'begin_segment': point1, 'end_segment': point2}


def get_mid_point_of_segment(segment):
    x1 = get_x(segment['begin_segment'])
    x2 = get_x(segment['end_segment'])
    y1 = get_y(segment['begin_segment'])
    y2 = get_y(segment['end_segment'])
    return make_decart_point((x1 + x2) / 2, (y1 + y2) / 2)


if __name__ == '__main__':
    segment1 = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
    assert make_decart_point(1.5, 1) == get_mid_point_of_segment(segment1)
    segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
    assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)
