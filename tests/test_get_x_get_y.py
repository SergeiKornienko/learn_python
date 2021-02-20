from functions.get_x_get_y import make_decart_point
from functions.segments import is_parallel_with_x, is_parallel_with_y, make_segment


def test_segment():
    point1 = make_decart_point(3, 2)
    point2 = make_decart_point(0, 0)
    point3 = make_decart_point(3, -5)
    assert is_parallel_with_y(make_segment(point1, point2)) is False
    assert is_parallel_with_y(make_segment(point1, point3)) is True
    assert is_parallel_with_x(make_segment(point2, point3)) is False
