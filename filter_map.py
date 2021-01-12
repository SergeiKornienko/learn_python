from math import sqrt


def filter_map(func, items):
    result = []
    for item in items:
        predicate, mean = func(item)
        if predicate:
            result.append(mean)
    return result


if __name__ == '__main__':
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)


    empty = filter_map(safe_sqrt, [])
    assert not empty
    assert isinstance(empty, list)
    assert filter_map(safe_sqrt, [4, -5, -2, 9]) == [2.0, 3.0]  # noqa: WPS221
    print(filter_map(safe_sqrt, [4, -5, -2, 9]))
