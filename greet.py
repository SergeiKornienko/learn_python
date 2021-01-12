def greet(name, *args):
    greeting = ''.join(['Hello, ', name])
    for n in args:
        greeting = ' and '.join([greeting, n])
    return ''.join([greeting, '!'])


if __name__ == '__main__':
    print(greet('Moe', 'Mary'))

    assert greet('Bob') == 'Hello, Bob!'
    assert greet('Bob', 'Ann') == 'Hello, Bob and Ann!'
    assert greet('Bob', 'Ann', 'Moe') == 'Hello, Bob and Ann and Moe!'