def greet(name, *args):
    greeting = ''.join(['Hello, ', name])
    for n in args:
        greeting = ' and '.join([greeting, n])
    return ''.join([greeting, '!'])
