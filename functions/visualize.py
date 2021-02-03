from collections import Counter


def visualize(coins, bar_char='₽'):  # noqa: WPS210
    """Visualize money in a money box."""
    # BEGIN (write your solution here)
    count_of_coins = dict(Counter(coins))
    list_coins = sorted(count_of_coins.keys())
    coins = ' '.join(map(
        lambda coin:
        ''.join([str(coin), ' ']) if len(str(coin)) == 1 else str(coin),
        list_coins,
    ))
    head = '\n'.join([('-' * len(coins)), coins])
    graf = ''
    i = 0
    while i <= max(count_of_coins.values()):
        graf = ''.join([
            to_string(i, count_of_coins, bar_char=bar_char),
            '\n',
            graf.rstrip(),
        ])
        i += 1
    return ''.join([graf, '\n', head])


def to_string(i, count_of_coins, bar_char='₽'):
    list_coins = sorted(count_of_coins.keys())
    string = ''
    for coin in list_coins:
        mean = count_of_coins[coin]
        if mean == i and mean > 9:
            string = ''.join([string, str(mean), " "])
        elif mean == i:
            string = ''.join([string, str(mean), "  "])
        elif mean < i:
            string = ''.join([string, "   "])
        elif mean > i:
            string = ''.join([string, bar_char * 2, " "])
    return string[:-1]
# END
