def updated(data, **kwargs):
    new_data = data.copy()
    for key, arg in kwargs.items():
        new_data[key] = arg
    return new_data


if __name__ == '__main__':
    d = {'a': 1, 'b': False}
    print(updated(d, a=2, b=True, c=None))

    old = {'a': 1, 'b': None, 2: 4}
    copy_of_old = old.copy()
    assert updated(old) is not old
    assert updated(old, a=2) == {'a': 2, 'b': None, 2: 4}
    assert old == copy_of_old, "Old dict should stay unchanged!"
    assert updated({}, foo='bar', bar=42) == {'foo': 'bar', 'bar': 42}
