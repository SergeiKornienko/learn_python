from operator import add, mul


def partial_apply(func, arg1):
    def inner(arg2):
        return func(arg1, arg2)
    return inner


def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner


if __name__ == '__main__':
    assert list(
        map(partial_apply(add, 10), [1, 2, 3]),  # noqa: WPS221
    ) == [11, 12, 13]

    assert list(
        map(partial_apply(mul, '*'), [2, 3, 4]),  # noqa: WPS221
    ) == [
               '**',
               '***',
               '****',
           ]
    assert flip(mul)(3, '*') == '***'
    assert list(
        map(partial_apply(flip(mul), 5), "!?&"),
    ) == [
               '!!!!!',
               '?????',
               '&&&&&',
           ]