def is_even(num):
    return num % 2 == 0


def same_parity_filter(items):
    result = []
    for item in items:
        if is_even(item) == is_even(items[0]):
            result.append(item)
    return result
