# Реализуйте функцию find_index_of_nearest,
# которая принимает на вход список чисел и
# искомое число. Задача функции — найти в списке
# ближайшее число к искомому и вернуть его индекс.
#
# Если в списке содержится несколько чисел,
# одновременно являющихся ближайшими к искомому
# числу, то возвращается наименьший из индексов
# ближайших чисел.
#
# Примеры
# >>> find_index_of_nearest(2, []) is None
# True
# >>> find_index_of_nearest(0, [15, 10, 3, 4])
# 2
# >>> find_index_of_nearest(4, [7, 5, 3, 2])
# 1
# >>> find_index_of_nearest(4, [7, 5, 4, 4, 3])
# 2
def find_index_of_nearest(num, nums):
    if nums:
        sub = list(map(lambda x: abs(x - num), nums))
        return sub.index(min(sub))


if __name__ == '__main__':
    print(find_index_of_nearest(4, [7, 5, 4, 4, 3, 6]))

    assert find_index_of_nearest(2, []) is None
    assert find_index_of_nearest(0, [10]) == 0
    assert find_index_of_nearest(0, [10, 15]) == 0
    assert find_index_of_nearest(1, [15, 10]) == 1
    assert find_index_of_nearest(12, [15, 10]) == 1
    assert find_index_of_nearest(0, [15, 10, 3, 4]) == 2
    assert find_index_of_nearest(4, [7, 5, 3, 2]) == 1
    assert find_index_of_nearest(4, [7, 5, 4, 4, 3, 6]) == 2
