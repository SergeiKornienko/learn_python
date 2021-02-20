from classes.color import Color, rgb


def test_color_attributes():
    assert hasattr(Color, 'red')  # noqa: WPS421
    assert hasattr(Color, 'green')  # noqa: WPS421
    assert hasattr(Color, 'blue')  # noqa: WPS421


def test_color_values():
    assert Color.red == rgb(255, 0, 0)
    assert Color.green == rgb(0, 255, 0)
    assert Color.blue == rgb(0, 0, 255)
