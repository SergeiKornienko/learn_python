from functools import reduce
from operator import abs, getitem


def keep_truthful(items):
    return filter(None, items)


def abs_sum(list_nums):
    return sum(map(abs, list_nums))


def walk(data, path):
    return reduce(getitem, path, data)


if __name__ == '__main__':
    FALSES = (False, (), None, '', 0)
    TRUTHS = (True, (1,), '!', -5)
    assert list(keep_truthful(FALSES)) == [], (
        'All falsy values sholud be filtered out!'
    )
    assert list(keep_truthful(TRUTHS)) == list(TRUTHS), (
        'All truthful values sholud be keeped!'
    )
    assert list(keep_truthful([0, 1, 0])) == [1]
    assert abs_sum([0]) == 0
    assert abs_sum((-42,)) == 42
    assert abs_sum([-3, -2, -1, 0, 1, 2, 3]) == 12  # noqa: WPS221
    city = {
        'Pine': {
            '5': 'School #42',
        },
        'Elm': {
            '13': {
                '1': 'Appartments #2, Elm st.13',
            },
        },
    }
    assert walk(city, ['Pine', '5']) == city['Pine']['5']
    path = ['Elm', '13', '1']
    assert walk(city, path) == city['Elm']['13']['1']
