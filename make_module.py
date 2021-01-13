def make_module(step=1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}


if __name__ == '__main__':
    assert make_module()['inc'].__name__ == '<lambda>', (
        'Increment function should be the lambda!'
    )
    assert make_module()['dec'].__name__ == '<lambda>', (
        'Decrement function should be the lambda!'
    )

    assert make_module()['inc'](0) == 1
    assert make_module()['dec'](5) == 4

    inc, dec = map(make_module(step=5).get, ['inc', 'dec'])
    assert inc(inc(inc(dec(0)))) == 10
