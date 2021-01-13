from functools import wraps


def memoizing(count):
    def wrapper(func):
        means = {}

        @wraps(func)
        def inner(arg):
            if arg in means:
                return means.get(arg)
            result = func(arg)
            results = list(means.keys())
            if len(results) == count:
                means.pop(results[0])
            means[arg] = result
            return result

        return inner
    return wrapper


if __name__ == '__main__':
    arguments = []

    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1
    print(inc(inc(inc(0))))

    arguments = []


    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1


    assert inc(inc(inc(0))) == 3
    assert arguments == [0, 1, 2]
    _ = inc(inc(inc(0)))
    assert arguments == [0, 1, 2], "All results should be got from memory!"
    assert inc(10) == 11
    assert arguments == [0, 1, 2, 10], "New argument should be added!"
    assert inc(0) == 1
    assert arguments == [0, 1, 2, 10, 0], (
        "Result for zero should be recalculated!",
    )

    @memoizing(3)
    def foo():
        """Return bar."""


    assert foo.__name__ == "foo", (
        "Wrapper should preserve function's name!",
    )
    assert foo.__doc__ == "Return bar.", (
        "Wrapper should preserve function's docstring!",
    )
