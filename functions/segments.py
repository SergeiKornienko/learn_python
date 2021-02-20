from functions.get_x_get_y import get_x, get_y


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
