from functions.visualize import visualize

MONEY = (  # noqa: WPS317
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)


def test_visualize():
    assert visualize(MONEY) == """
   6             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2  2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291

    assert visualize(MONEY, bar_char='$') == """
   6             
   $$          5 
4  $$          $$
$$ $$          $$
$$ $$ 2  2  2  $$
$$ $$ $$ $$ $$ $$
$$ $$ $$ $$ $$ $$
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291
