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
