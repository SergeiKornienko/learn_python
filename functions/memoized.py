def memoized(func):
    means = {}

    def inner(arg):
        if arg in means:
            return means.get(arg)
        result = func(arg)
        means[arg] = result
        return result
    return inner
