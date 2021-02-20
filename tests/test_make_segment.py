from functions.points import make_decart_point
from functions.make_segment import get_mid_point_of_segment, make_segment


def test_segments():
    segment1 = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
    assert make_decart_point(1.5, 1) == get_mid_point_of_segment(segment1)
    segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
    assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)
