def is_odd(num):
    return False if num % 2 == 0 else is_even(num + 1)


def is_even(num):
    return True if num % 2 == 0 else is_odd(num + 1)


if __name__ == '__main__':
    assert not is_odd(42)
    assert is_odd(99)
    assert not is_even(99)
    assert is_even(42)
