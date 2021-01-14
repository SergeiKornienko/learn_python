# Реализуйте функцию same_parity_filter, которая
# принимает на вход список и возвращает новый
# список, состоящий из элементов, у которых такая
# же чётность, как и у первого элемента исходного
# списка.
#
# Примеры
# >>> same_parity_filter([])
# []
# >>> same_parity_filter([2, 0, 1, -3, 10, -2])
# [2, 0, 10, -2]
# >>> same_parity_filter([-1, 0, 1, -3, 10, -2])
# [-1, 1, -3]
def is_even(num):
    return num % 2 == 0


def same_parity_filter(items):
    result = []
    for item in items:
        if is_even(item) == is_even(items[0]):
            result.append(item)
    return result


if __name__ == '__main__':
    print(same_parity_filter([5, 0, 1, -3, 10]))
    assert same_parity_filter([5, 0, 1, -3, 10]) == [5, 1, -3]
    assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
    assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
    assert same_parity_filter([10, -1.5, 1.3, -3, 25, -2]) == [10, -2]
    assert same_parity_filter([]) == []
