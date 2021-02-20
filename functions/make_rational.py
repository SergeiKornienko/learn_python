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
