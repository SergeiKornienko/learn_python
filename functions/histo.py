from collections import Counter


def histo(samples, min_value=None, max_value=None, bar_char='#'):
    """Draws a horizontal histogram."""
    # BEGIN (write your solution here)
    if not min_value:
        min_value = min(samples)
    if not max_value:
        max_value = max(samples)
    c = dict(Counter(samples))
    graphic = []
    for n in range(min_value, max_value + 1):
        if n in c.keys():
            string = ''.join([str(n), '|', bar_char * c[n], ' ', str(c[n])])
        else:
            string = ''.join([str(n), '|'])
        graphic.append(string)
    return '\n'.join(graphic)
    # END
