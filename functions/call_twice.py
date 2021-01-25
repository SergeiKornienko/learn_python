def call_twice(func, *args, **kwargs):
    return func(*args, **kwargs), func(*args, **kwargs)
