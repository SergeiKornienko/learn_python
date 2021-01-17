def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None
# Реализуйте абстракцию (набор функций) для работы с прямоугольниками,
# стороны которого всегда параллельны осям. Прямоугольник может
# располагаться в любом месте координатной плоскости.
#
# При такой постановке, достаточно знать только три параметра для
# однозначного задания прямоугольника на плоскости: координаты левой-верхней
# точки, ширину и высоту. Зная их, мы всегда можем построить прямоугольник
# одним единственным способом.
#
#       |
#     4 |    точка   ширина
#       |       *-------------
#     3 |       |            |
#       |       |            | высота
#     2 |       |            |
#       |       --------------
#     1 |
#       |
# ------|---------------------------
#     0 |  1   2   3   4   5   6   7
#       |
#       |
#       |
# Основной интерфейс:
#
# make_rectangle (конструктор) – создает прямоугольник. Принимает
# параметры: левую-верхнюю точку, ширину и высоту. Ширина и высота –
# положительные числа.
# Селекторы get_start_point, get_width и get_height
# contains_origin – проверяет, принадлежит ли центр координат
# прямоугольнику (не лежит на границе прямоугольника, а находится внутри).
# Чтобы в этом убедиться, достаточно проверить, что все вершины
# прямоугольника лежат в разных квадрантах (их можно высчитать
# в момент проверки).
# # Создание прямоугольника:
# # p - левая верхняя точка
# # 4 - ширина
# # 5 - высота
# #
# # p    4
# # -----------
# # |         |
# # |         | 5
# # |         |
# # -----------
#
# >>> p = make_decart_point(0, 1)
# >>> rectangle = make_rectangle(p, 4, 5)
#
# >>> contains_origin(rectangle)
# False
#
# >>> rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
# >>> contains_origin(rectangle2)
# True


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


if __name__ == '__main__':
    p = make_decart_point(-4, 3)
    rectangle1 = make_rectangle(p, 5, 4)
    assert contains_origin(rectangle1)
    rectangle2 = make_rectangle(p, 5, 2)
    assert not contains_origin(rectangle2)
    rectangle3 = make_rectangle(p, 2, 2)
    assert not contains_origin(rectangle3)
    rectangle4 = make_rectangle(p, 4, 3)
    assert not contains_origin(rectangle4)
    point = make_decart_point(0, 1)
    rectangle = make_rectangle(point, 4, 5)
    assert not contains_origin(rectangle)
