from functions import make_rational

rat1 = make_rational.make(3, 9)
rat2 = make_rational.make(10, 3)
rat3 = make_rational.make(-4, 16)
rat4 = make_rational.make(12, 5)


def test_make_rational1():
    assert make_rational.get_numer(rat1) == 1
    assert make_rational.get_denom(rat1) == 3
    assert make_rational.add(rat1, rat2) == make_rational.make(11, 3)
    assert make_rational.sub(rat1, rat2) == make_rational.make(-3, 1)


def test_make_rational2():
    assert make_rational.get_numer(rat3) == -1
    assert make_rational.get_denom(rat3) == 4
    assert make_rational.add(rat3, rat4) == make_rational.make(43, 20)
    assert make_rational.sub(rat3, rat4) == make_rational.make(-53, 20)


def test_to_str():
    assert make_rational.to_str(rat1) == "1/3"
    assert make_rational.to_str(rat3) == "-1/4"
