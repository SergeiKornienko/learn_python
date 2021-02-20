import math


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
