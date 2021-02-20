from functions.convert import convert


def test_convert():
    assert convert([]) == {}
    assert convert([['key', 'value']]) == {'key': 'value'}
    assert convert(
        [
            ['key2', 'value2'],
            ['key3', 'value3'],
        ]) == {'key2': 'value2', 'key3': 'value3'}
    tree = [
        ['key4', 'value4'],
        ['anotherKey', [
            ['key7', False],
            ['innerKey', []],
        ],
        ],
        ['key6', None],
        ['anotherKey2', [
            ['wow', [['one', 'two'], ['three', 'four']]],
            ['key5', True],
        ],
        ],
    ]
    expected = {
        'key4': 'value4',
        'anotherKey': {'key7': False, 'innerKey': {}},
        'key6': None,
        'anotherKey2': {'wow': {'one': 'two', 'three': 'four'}, 'key5': True},
    }
    assert convert(tree) == expected
