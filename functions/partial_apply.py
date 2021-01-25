def partial_apply(func, arg1):
    def inner(arg2):
        return func(arg1, arg2)
    return inner


def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner
