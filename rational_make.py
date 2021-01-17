# Реализуйте абстракцию для работы с рациональными
# числами включающую в себя следующие функции:
#
# Конструктор make — принимает на вход числитель и
# знаменатель, возвращает дробь.
# Селектор get_numer — возвращает числитель
# Селектор get_denom — возвращает знаменатель
# Сложение add — складывает переданные дроби
# Вычитание sub — находит разность между двумя дробями
# Не забудьте реализовать нормализацию дробей удобным д
# ля вас способом.
#
# Примеры работы:
#
# >>> import rational
#
# >>> rat1 = make(3, 9)
# >>> get_numer(rat1)
# 1
# >>> get_denom(rat1)
# 3
# >>> rat2 = make(10, 3)
# >>> rat3 = add(rat1, rat2)
# >>> to_str(rat3)
# 11/3
# >>> rat4 = sub(rat1, rat2)
# >>> to_str(rat4)
# -3/1
import math


def to_str(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))


# BEGIN (write your solution here)
def make(numer, denom):
    diviser = math.gcd(numer, denom)
    return {'numer': numer // diviser, 'denom': denom // diviser}


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denom']


def add(rat1, rat2):
    numer_rat1 = get_numer(rat1)
    denom_rat1 = get_denom(rat1)
    numer_rat2 = get_numer(rat2)
    denom_rat2 = get_denom(rat2)
    return make(
        numer_rat1 * denom_rat2 + numer_rat2 * denom_rat1,
        denom_rat1 * denom_rat2,
    )


def sub(rat1, rat2):
    numer_rat1 = get_numer(rat1)
    denom_rat1 = get_denom(rat1)
    numer_rat2 = get_numer(rat2)
    denom_rat2 = get_denom(rat2)
    return make(
        numer_rat1 * denom_rat2 - numer_rat2 * denom_rat1,
        denom_rat1 * denom_rat2,
    )
# END


if __name__ == '__main__':
    rat1 = make(3, 9)
    rat2 = make(10, 3)
    rat3 = make(-4, 16)
    rat4 = make(12, 5)
    assert get_numer(rat1) == 1
    assert get_denom(rat1) == 3
    assert add(rat1, rat2) == make(11, 3)
    assert sub(rat1, rat2) == make(-3, 1)
    assert get_numer(rat3) == -1
    assert get_denom(rat3) == 4
    assert add(rat3, rat4) == make(43, 20)
    assert sub(rat3, rat4) == make(-53, 20)
    assert to_str(rat1) == "1/3"
    assert to_str(rat3) == "-1/4"
