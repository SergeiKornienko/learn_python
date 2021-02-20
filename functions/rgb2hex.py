def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex2rgb(str_rgb):
    return {
        'r': int(str_rgb[1:3], 16),
        'g': int(str_rgb[3:5], 16),
        'b': int(str_rgb[5:], 16),
    }


if __name__ == '__main__':
    cases = [
        ('#000000', (0, 0, 0)),
        ('#ffffff', (255, 255, 255)),
        ('#00840c', (0, 132, 12)),
        ('#24ab00', (36, 171, 0)),
        ('#c60123', (198, 1, 35)),
        ('#543fab', (84, 63, 171)),
        ('#f700de', (247, 0, 222)),
    ]
    for hex_, rgb in cases:
        r, g, b = rgb
        assert rgb2hex(r, g, b) == hex_
    assert rgb2hex(r=84, g=63, b=171) == '#543fab'
    assert rgb2hex(r=247, b=222, g=0) == '#f700de'
    for hex_, rgb in cases:
        r, g, b = rgb
        assert hex2rgb(hex_) == {'r': r, 'g': g, 'b': b}
