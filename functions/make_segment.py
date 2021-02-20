from functions.points import get_x, get_y, make_decart_point


def make_segment(point1, point2):
    return {'begin_segment': point1, 'end_segment': point2}


def get_mid_point_of_segment(segment):
    x1 = get_x(segment['begin_segment'])
    x2 = get_x(segment['end_segment'])
    y1 = get_y(segment['begin_segment'])
    y2 = get_y(segment['end_segment'])
    return make_decart_point((x1 + x2) / 2, (y1 + y2) / 2)
