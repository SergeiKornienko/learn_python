from classes.RGB import RGB, red, green, blue


def rgb2tuple(rgb):
    return rgb.red, rgb.green, rgb.blue


def test_instances():
    assert isinstance(red, RGB)
    assert isinstance(green, RGB)
    assert isinstance(blue, RGB)


def test_attributes():
    assert rgb2tuple(red) == (255, 0, 0)
    assert rgb2tuple(green) == (0, 255, 0)
    assert rgb2tuple(blue) == (0, 0, 255)
