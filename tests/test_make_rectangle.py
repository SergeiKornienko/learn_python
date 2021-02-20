from functions.points import make_decart_point
from functions.make_rectangle import contains_origin, make_rectangle


def test_rectangle():
    p = make_decart_point(-4, 3)
    rectangle1 = make_rectangle(p, 5, 4)
    assert contains_origin(rectangle1)

    rectangle2 = make_rectangle(p, 5, 2)
    assert not contains_origin(rectangle2)

    rectangle3 = make_rectangle(p, 2, 2)
    assert not contains_origin(rectangle3)

    rectangle4 = make_rectangle(p, 4, 3)
    assert not contains_origin(rectangle4)


def test_cross_zero():
    point = make_decart_point(0, 1)
    rectangle = make_rectangle(point, 4, 5)
    assert not contains_origin(rectangle)