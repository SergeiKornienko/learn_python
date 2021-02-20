def compose(func1, func2):
    return lambda arg: func1(func2(arg))
