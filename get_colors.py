def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


# BEGIN (write your solution here)
def get_colors():
    return {'red': rgb(red=255), 'green': rgb(green=255), 'blue': rgb(blue=255)}
# END


if __name__ == '__main__':
    colors = get_colors()
    print(set(colors.keys()) == {'red', 'green', 'blue'})
    assert set(colors.keys()) == {'red', 'green', 'blue'}
    assert colors['red'] == rgb(red=255)
    assert colors['green'] == rgb(green=255)
    assert colors['blue'] == rgb(blue=255)
