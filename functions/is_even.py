def is_odd(num):
    return False if num % 2 == 0 else is_even(num + 1)


def is_even(num):
    return True if num % 2 == 0 else is_odd(num + 1)
