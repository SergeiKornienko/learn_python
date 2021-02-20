from functions.points import get_quadrant, get_x, get_y, make_decart_point


# BEGIN (write your solution here)
def make_rectangle(start_point, width, height):
    return {
        'start_point': start_point,
        'width': width,
        'heigth': height,
    }


def get_start_point(rectangle):
    return rectangle['start_point']


def get_width(rectangle):
    return rectangle['width']


def get_heigth(rectangle):
    return rectangle['heigth']


def get_right_up_point(rectangle):
    x = get_x(get_start_point(rectangle)) + get_width(rectangle)
    y = get_y(get_start_point(rectangle))
    return make_decart_point(x, y)


def get_right_down_point(rectangle):
    x = get_x(get_start_point(rectangle)) + get_width(rectangle)
    y = get_y(get_start_point(rectangle)) - get_heigth(rectangle)
    return make_decart_point(x, y)


def get_left_down_point(rectangle):
    x = get_x(get_start_point(rectangle))
    y = get_y(get_start_point(rectangle)) - get_heigth(rectangle)
    return make_decart_point(x, y)


def get_points_rectangle(rectangle):
    return [
        get_start_point(rectangle),
        get_right_up_point(rectangle),
        get_right_down_point(rectangle),
        get_left_down_point(rectangle),
    ]


def contains_origin(rectangle):
    quadtants = list(map(get_quadrant, get_points_rectangle(rectangle)))
    return len(set(quadtants)) == 4
# END
